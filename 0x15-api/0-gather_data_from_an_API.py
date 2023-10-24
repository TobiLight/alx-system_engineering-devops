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
        c = "completed=true"

        try:
            user = requests.\
                get("https://jsonplaceholder.typicode.com/users/{}".
                    format(userID))
            # raise an error if it occurs
            user.raise_for_status()
            completed = requests.\
                get("https://jsonplaceholder.typicode.com/todos?userId={}&{}".
                    format(userID, c))
            # # raise an error if it occurs
            completed.raise_for_status()
            todos = requests.\
                get("https://jsonplaceholder.typicode.com/todos?userId={}".
                    format(userID))
            # raise an error if it occurs
            todos.raise_for_status()
            user = user.json()
            total_todos = len(todos.json())
            completed_todos = len(completed.json())
            completed = completed.json()

            print("Employee {} is done with tasks({}/{}):".
                  format(user['name'], completed_todos, total_todos))
            for todo in completed:
                if str(todo['userId']) == userID:
                    print("\t {}".format(todo['title']))
        except requests.exceptions.RequestException as e:
            pass


# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         userID = sys.argv[1]
#         response = requests.\
#             get("https://jsonplaceholder.typicode.com/users/{}".
#                 format(userID))
#         todo_response = requests.\
#             get("https://jsonplaceholder.typicode.com/todos")

#         try:
#             response.raise_for_status()
#             todo_response.raise_for_status()
#             user = response.json()
#             todos = todo_response.json()
#             completed = 0
#             total = 0
#             todos_title = []
#             for todo in todos:
#                 if str(todo['userId']) == userID:
#                     total += 1
#                 if str(todo['userId']) == userID and todo['completed'] is True:
#                     completed += 1
#                     todos_title.append(todo['title'])
#             print("Employee {} is done with tasks({}/{}):".
#                   format(user['name'], completed, total))
#             for todo in todos_title:
#                 print("\t {}".format(todo))
#         except requests.exceptions.RequestException as e:
#             pass
