#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to CSV"""


from csv import DictWriter, QUOTE_ALL
from requests import get
from sys import argv

if __name__ == "__main__":
    main_url = "https://jsonplaceholder.typicode.com"
    employee_id = argv[1]
    todo_url = f"{main_url}/user/{employee_id}/todos"
    name_url = f"{main_url}/users/{employee_id}"

    # Make requests
    todo_response = get(todo_url)
    todo_result = todo_response.json()

    name_response = get(name_url)
    name_result = name_response.json()

    if todo_response.status_code != 200 or name_response.status_code != 200:
        print("An error occurred while fetching data")
        exit()

    todo_list = []
    for todo in todo_result:
        todo_dict = {
            "user_ID": employee_id,
            "username": name_result.get("username"),
            "completed": todo.get("completed"),
            "task": todo.get("title")
        }
        todo_list.append(todo_dict)

    with open(f"{employee_id}.csv", 'w', newline='') as f:
        header = ["user_ID", "username", "completed", "task"]
        writer = DictWriter(f, fieldnames=header, quoting=QUOTE_ALL)
        writer.writeheader()
        writer.writerows(todo_list)
