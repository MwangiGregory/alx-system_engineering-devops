#!/usr/bin/python3
"""This script accepts an employee ID and returns information
about his/her TODO list progress"""
if __name__ == "__main__":
    import json
    import requests

    url = 'https://jsonplaceholder.typicode.com/'
    with open('todo_all_employees.json', 'a', encoding='utf-8') as f:
        users = requests.get(url + "users").json()
        all_todos = {}
        for user in users:
            username = user.get('username')
            user_id = user.get('id')
            tasks = requests.get(url + "todos",
            params={'userId': user_id}).json()
            user_tasks = []
            for task in tasks:
                temp = {}
                temp['username'] = username
                temp['task'] = task.get('title')
                temp['completed'] = task.get('completed')
                user_tasks.append(temp)
            all_todos[user_id] = user_tasks
        json.dump(all_todos, f)