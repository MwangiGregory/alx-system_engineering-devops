#!/usr/bin/python3
"""This script accepts an employee ID and returns information
about his/her TODO list progress"""
if __name__ == "__main__":
    import json
    import requests

    with open('todo_all_employees.json', 'a', encoding='utf-8') as f:
        users = requests.get('https://jsonplaceholder.typicode.com/users')
        users = users.json()
        all_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
        all_todos = all_todos.json()

        all_tasks = {}
        for user in users:
            usr_name = user.get('username')
            user_id = user.get('id')
            user_tasks = []
            for todo in all_todos:
                if todo.get('userId') == user_id:
                    task = {}
                    task['username'] = usr_name
                    task['task'] = todo.get('title')
                    task['completed'] = todo.get('completed')
                    user_tasks.append(task)
            all_tasks[user_id] = user_tasks
        json.dump(all_tasks, f)
