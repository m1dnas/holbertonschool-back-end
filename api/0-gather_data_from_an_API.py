#!/usr/bin/python3
"""
Python script that, using the jsonplaceholder REST API, for a given employee
ID, returns information about his/her TO-DO list progress.
The script must accept an integer as a parameter, which is the employee ID.
"""
import requests
from sys import argv

if __name__ == '__main__':

    finished_tasks = 0
    total_tasks = 0

    user_request = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json()
    todos_request = requests.get(
        'http://jsonplaceholder.typicode.com/todos').json()
    user_todos_list = [x for x in todos_request if x.get(
        'userId') == int(argv[1])]

    user_complete_list = [
        x for x in user_todos_list if x.get('completed') is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user_request.get('name'),
        len(user_complete_list),
        len(user_todos_list)))

    for task in user_complete_list:
        print("\t " + task.get('title'))
