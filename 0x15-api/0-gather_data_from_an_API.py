#!/usr/bin/python3
"""This script accepts an employee ID and returns information
about his/her TODO list progress"""
if __name__ == "__main__":
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

    count = 0
    for todo in todos:
        if todo.get('completed'):
            count += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, count, todos_total))
    for todo in todos:
        if todo.get('completed'):
            print("\t {}".format(todo.get('title')))
