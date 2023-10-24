#!/usr/bin/python3
# File: 2-export_to_JSON.py
# Author: Oluwatobiloba Light
"""
Returns information about an employee's TODO list progress for a
given employee ID and exports data in JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        userID = sys.argv[1]

        try:
            user = requests.\
                get("https://jsonplaceholder.typicode.com/users/{}".
                    format(userID))
            user.raise_for_status()
            user = user.json()
            todos = requests.\
                get("https://jsonplaceholder.typicode.com/todos?userId={}".
                    format(userID))
            # raise an error if it occurs
            todos.raise_for_status()
            todos = todos.json()
            filename = "{}.json".format(userID)
            formatted_data = {}
            formatted_data[userID] = []
            for todo in todos:
                if str(todo['userId']) == userID:
                    formatted_data[userID].\
                        append({"task": todo['title'],
                                "completed": todo['completed'],
                                "username": user['username']})
            with open(filename, 'w', encoding="utf-8") as file:
                json.dump(formatted_data, file)
        except requests.exceptions.RequestException as e:
            pass
