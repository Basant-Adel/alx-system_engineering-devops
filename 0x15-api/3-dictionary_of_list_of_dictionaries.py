#!/usr/bin/python3
""" Python script -> export data in the CSV format """
import json
import requests


if __name__ == "__main__":
    """ Name of the employee """
    URL = 'https://jsonplaceholder.typicode.com'
    ulist = requests.get(f'{URL}/users').json()
    tlist = requests.get(f'{URL}/todos').json()
    alltodoemp = {}
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
        alltodoemp[user_id] = emplist
    with open("alltodoemp.json", "w") as outfile:
        json.dump(alltodoemp, outfile)
