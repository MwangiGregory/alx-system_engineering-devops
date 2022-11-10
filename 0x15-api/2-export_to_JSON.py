#!/usr/bin/python3
"""Returns information about an employee's TODO list progress"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    employee_id = sys.argv[1]
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos = requests.get(todos_url, params={"userId": employee_id})
    user = requests.get(users_url, params={"id": employee_id})
    employee_name = user.json()[0].get("username")

    tasks_dict = {}
    tasks_dict[str(employee_id)] = []
    for todo in todos.json():
        temp = {}
        temp['task'] = todo.get('title')
        temp['completed'] = todo.get('completed')
        temp['username'] = employee_name
        tasks_dict[str(employee_id)].append(temp)
    with open(str(employee_id) + ".json", 'w', encoding='utf-8') as f:
        json.dump(tasks_dict, f)
