#!/usr/bin/python3
"""This script accepts an employee ID and returns information
about his/her TODO list progress"""
if __name__ == "__main__":
    import json
    import requests
    import sys

    employee_id = sys.argv[1]
    payload = {'userId': employee_id}
    users_response = requests.get('https://jsonplaceholder.typicode.com/users',
                                  params={'id': employee_id})
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos',
                                  params=payload)
    todos = todos_response.json()
    user = users_response.json()
    todos_total = len(todos)
    employee_name = user[0].get('name')
    username = user[0].get('username')

    count = 0
    for todo in todos:
        if todo.get('completed'):
            count += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, count, todos_total))
    for todo in todos:
        if todo.get('completed'):
            print("\t {}".format(todo.get('title')))

    with open('{}.csv'.format(employee_id), 'a', encoding='utf-8') as f:
        for index, todo in enumerate(todos):
            f.write('\"{}\",\"{}\",\"{}\",\"{}\"{}'.format(
                    employee_id, username,
                    str(todo.get('completed')),
                    todo.get('title'),
                    '\n' if index < len(todos) - 1 else ''))
    with open('{}.json'.format(employee_id), 'a', encoding='utf-8') as f:
        tasks = []
        for todo in todos:
            temp = {}
            temp['task'] = todo.get('title')
            temp['completed'] = todo.get('completed')
            temp['username'] = username
            tasks.append(temp)
        user_tasks = {}
        user_tasks[str(employee_id)] = tasks
        print(user_tasks)
        json.dump(user_tasks, f)
