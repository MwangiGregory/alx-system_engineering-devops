#!/usr/bin/python3
"""Returns information about an employee's TODO list progress"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    employee_id = sys.argv[1]
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos = requests.get(todos_url, params={"userId": employee_id})
    user = requests.get(users_url, params={"id": employee_id})
    employee_name = user.json()[0].get("username")

    fieldnames = ['userId', 'name', 'completed', 'title']
    todo_data = []
    for todo in todos.json():
        temp = {}
        temp['userId'] = str(employee_id)
        temp['name'] = employee_name
        temp['completed'] = str(todo.get('completed'))
        temp['title'] = todo.get('title')
        todo_data.append(temp)
    csv_file = str(employee_id) + '.csv'
    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerows(todo_data)
