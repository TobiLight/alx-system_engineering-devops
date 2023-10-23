#!/usr/bin/python3
# File: 0-gather_data_from_an_API.py
# Author: Oluwatobiloba Light
"""
Returns information about an employee's TODO list progress for a
given employee ID.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        userID = sys.argv[1]
        response = requests.\
            get("https://jsonplaceholder.typicode.com/users/{}".format(userID))
        todo_response = requests.\
            get("https://jsonplaceholder.typicode.com/todos")
        try:
            response.raise_for_status()
            todo_response.raise_for_status()
            user = response.json()
            todos = todo_response.json()
            completed = 0
            total = 0
            todos_title = []
            for todo in todos:
                if str(todo['userId']) == userID:
                    total += 1
                if str(todo['userId']) == userID and todo['completed'] is True:
                    completed += 1
                    todos_title.append(todo['title'])
            print("Employee {} is done with tasks({}/{}):".
                  format(user['name'], completed, total))
            for todo in todos_title:
                print("\t {}".format(todo))
        except requests.exceptions.RequestException as e:
            pass
