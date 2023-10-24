#!/usr/bin/python3
# File: 1-export_to_CSV.py
# Author: Oluwatobiloba Light
"""
Returns information about an employee's TODO list progress for a
given employee ID and exports data in CSV format.
"""
import csv
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
            filename = "{}.csv".format(userID)
            with open(filename, 'w',  newline='', encoding="utf-8") as\
                    file:
                writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
                for todo in todos:
                    writer.writerow([str(todo['userId']),
                                     str(user['username']),
                                     str(todo['completed']),
                                     str(todo['title'])])
        except requests.exceptions.RequestException as e:
            pass
