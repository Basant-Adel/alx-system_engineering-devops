#!/usr/bin/python3
""" Python script -> export data in the JSON format """
import json
import requests
from sys import argv


if __name__ == "__main__":
    """ Name of the employee  """
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
    causer = {}
    for task in tlist:
        if task.get('userId') == user_ID:
            emplist.append({
                              "task": task.get('title'),
                              "completed": task.get('completed'),
                              "username": username, })
    causer[f"{user_ID}"] = emplist
    with open(f"{user_ID}.json", "w") as outfile:
        json.dump(causer, outfile)
