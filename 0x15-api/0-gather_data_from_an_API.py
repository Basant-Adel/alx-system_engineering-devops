#!/usr/bin/python3
""" Write Python script using this REST API -> for given employee ID """
import requests
from sys import argv

if __name__ == "__main__":
    """ Name of the employee """
    try:
        user_ID = int(argv[1])
    except Exception as a:
        exit()
    URL = 'https://jsonplaceholder.typicode.com'
    employee_data = requests.get(f'{URL}/users/{user_ID}').json()
    if employee_data == {}:
        exit()
    emp_name = employee_data.get('name')
    tlist = requests.get(f'{URL}/todos').json()
    ntap = 0
    done_ntap = 0
    plist = []
    for task in tlist:
        if task.get('userId') == user_ID:
            ntap += 1
            if task.get('completed'):
                done_ntap += 1
                plist.append(task.get('title'))
    print(f"Employee {emp_name} is done with tasks({done_ntap}/{ntap}):")
    for task in plist:
        print(f"\t {task}")
