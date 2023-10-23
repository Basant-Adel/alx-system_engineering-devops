#!/usr/bin/python3
""" Python script -> export data in CSV format """
import csv
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
    username = employee_data.get('username')
    tlist = requests.get(f'{URL}/todos').json()
    emplist = []
    for task in tlist:
        if task.get('userId') == user_ID:
            emplist.append(task)
    with open(f'{user_ID}.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for task in emplist:
            writer.writerow([f"{user_ID}", f"{username}",
                             f"{task.get('completed')}",
                             f"{task.get('title')}"])
