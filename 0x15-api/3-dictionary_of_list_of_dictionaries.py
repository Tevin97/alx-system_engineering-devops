#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to JSON"""


from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_result = get(users_url).json()

    big_dict = {}
    for user in users_result:
        user_id = user.get("id")
        my_url = "https://jsonplaceholder.typicode.com/users/"
        todos_url = f"{my_url}{user_id}/todos"

        todo_result = get(todos_url).json()

        todo_list = []
        for todo in todo_result:
            todo_dict = {
                "username": user.get("username"),
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            todo_list.append(todo_dict)

        big_dict[user_id] = todo_list

    with open("todo_all_employees.json", 'w') as f:
        dump(big_dict, f)
