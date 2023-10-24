#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

import requests
from sys import argv

if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'

    # Get employee ID from command-line argument
    if len(argv) < 2:
        print("Employee ID is required.")
        exit()

    employee_id = argv[1]

    todo_url = f"{main_url}/user/{employee_id}/todos"
    name_url = f"{main_url}/users/{employee_id}"

    todo_result = requests.get(todo_url).json()
    name_result = requests.get(name_url).json()

    todo_num = len(todo_result)
    todo_complete = sum(todo.get("completed", False) for todo in todo_result)
    name = name_result.get("name")
    myS = "is done with tasks"

    print("Employee {} {}({}/{}):".format(name, myS, todo_complete, todo_num))
    for todo in todo_result:
        if todo.get("completed"):
            print("\t {}".format(todo.get("title")))
