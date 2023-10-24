#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to JSON"""

from json import dump
from requests import get
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    todo_url = f"https://jsonplaceholder.typicode.com/user/{user_id}/todos"
    name_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todo_result = get(todo_url).json()
    name_result = get(name_url).json()

    todo_list = []
    for todo in todo_result:
        todo_dict = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": name_result.get("username")
        }
        todo_list.append(todo_dict)

    with open(f"{user_id}.json", 'w') as f:
        dump({user_id: todo_list}, f)
