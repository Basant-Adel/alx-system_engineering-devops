#!/usr/bin/python3
""" Python script -> export data in the CSV format """
import json
import requests


if __name__ == "__main__":
    """ Name of the employee """
    URL = 'https://jsonplaceholder.typicode.com'
    ulist = requests.get(f'{URL}/users').json()
    tlist = requests.get(f'{URL}/todos').json()
    todo_all_employees = {}
    for user in ulist:
        user_id = user.get('id')
        emplist = []
        for task in tlist:
            if task.get('userId') == user_id:
                emplist.append({
                                 "username": user.get('username'),
                                 "task": task.get('title'),
                                 "completed": task.get('completed')
                                 })
        todo_all_employees[user_id] = emplist
    with open("todo_all_employees.json", "w") as outfile:
        json.dump(todo_all_employees, outfile)
