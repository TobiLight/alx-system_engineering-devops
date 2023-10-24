#!/usr/bin/python3
# File: 3-dictionary_of_list_of_dictionaries.py
# Author: Oluwatobiloba Light
"""
Returns information about all employee's TODO list and exports data
in JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    filename = "todo_all_employees.json"
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    users = requests.get("https://jsonplaceholder.typicode.com/users")

    try:
        todos.raise_for_status()
        users.raise_for_status()
        todos = todos.json()
        users = users.json()
        json_data = {}
        for user in users:
            for todo in todos:
                if todo['userId'] == user['id']:
                    if user['id'] not in json_data:
                        json_data[user['id']] = []
                    json_data[user['id']].\
                        append({"username":
                                user['username'],
                                "task": todo['title'],
                                "completed": todo['completed']})
        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(json_data, file)
    except requests.exceptions.RequestException as e:
        pass
