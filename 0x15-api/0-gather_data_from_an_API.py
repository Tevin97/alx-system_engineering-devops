#!/usr/bin/python3

"""
Script retrieves info about an employee's TODO list progress from a REST API.
"""

import requests


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """

    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetching employee information
    employee_response = requests.get(f'{base_url}/users/{employee_id}')
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetching TODO list for the employee
    todo_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todo_data = todo_response.json()

    # Calculating progress
    total_tasks = len(todo_data)
    done_tasks = sum(task['completed'] for task in todo_data)
    my_cont = "is done with tasks"

    # Printing progress report
    print(f"Employee {employee_name} {my_cont} ({done_tasks}/{total_tasks}):")
    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    # Run the script with an employee ID of your choice
    employee_id = 1
    get_employee_todo_progress(employee_id)
