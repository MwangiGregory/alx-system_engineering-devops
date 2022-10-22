#!/usr/bin/python3
"""Returns information about an employee's TODO list progress"""

if __name__ == "__main__":
    import requests
    import sys

    employee_id = sys.argv[1]
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos = requests.get(todos_url, params={"userId": employee_id})
    user = requests.get(users_url, params={"id": employee_id})
    employee_name = user.json()[0].get("name")

    total_tasks = len(todos.json())
    tasks_done = 0

    for todo in todos.json():
        if todo.get('completed'):
            tasks_done += 1

    print('Employee {} is done with'.format(employee_name), end="")
    print(' tasks({}/{}):'.format(tasks_done, total_tasks))

    for todo in todos.json():
        if todo.get('completed'):
            print('\t {}'.format(todo.get("title")))

