#!/usr/bin/python3
"""
Python script that, using the jsonplaceholder REST API, for a given employee
ID, returns information about his/her TO-DO list progress.
The script must accept an integer as a parameter, which is the employee ID.
"""
import requests
import sys

if __name__ == '__main__':

    try:
        emp_id = int(sys.argv[1])
    except Exception:
        print("Please insert an integer as a parameter")
        exit()

    finished_tasks = 0
    total_tasks = 0

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    api_url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
        emp_id)

    user_response = requests.get(user_url).json().get('name')
    api_response = requests.get(api_url).json()

    for task in api_response:
        total_tasks += 1
        if task['completed'] is True:
            finished_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(user_response,
          finished_tasks, total_tasks))

    for task in api_response:
        if task['completed'] is True:
            print("\t {}".format(task['title']))
