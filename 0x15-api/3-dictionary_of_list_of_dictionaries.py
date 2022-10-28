#!/usr/bin/python3
"""Returns information about an employee's TODO list progress"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos = requests.get(todos_url).json()
    users = requests.get(users_url).json()

    user_dict = {}
    for user in users:
        userId = user.get('id')
        user_dict[userId] = []
        username = user.get('username')
        for todo in todos:
            if todo.get('userId') == userId:
                task = todo.get('title')
                completed = todo.get('completed')
                temp_dict = {}
                temp_dict['username'] = username
                temp_dict['task'] = task
                temp_dict['completed'] = completed
                user_dict[userId].append(temp_dict)
    with open('todo_all_employees.json', 'w', encoding='utf-8') as f:
        json.dump(user_dict, f)
