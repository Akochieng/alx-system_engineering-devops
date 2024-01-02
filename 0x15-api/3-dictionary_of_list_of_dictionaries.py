#!/usr/bin/python3
'''
Fetches data from remote web app and saves on a json file
'''
import json
from json import JSONDecodeError
import requests
from requests import exceptions
from requests.exceptions import HTTPError, Timeout, ConnectionError
from sys import argv
import sys


def export_tojson():
    '''
    Saves the employee id and todo list retrieved from remote web app
    to a json file
    '''
    userUrl = f"https://jsonplaceholder.typicode.com/users"
    secondUrl = f"https://jsonplaceholder.typicode.com/todos"
    tasks = dict()
    users = dict()
    try:
        userInfo = requests.get(userUrl)
        userInfo.raise_for_status()
        names = userInfo.json()
        for name in names:
            users.update({name['id']: name['username']})
    except (HTTPError, Timeout, ConnectionError, JSONDecodeError) as msg:
        sys.exit(msg)
    except requests.exceptions.RequestException as msg:
        sys.exit(msg)
    try:
        res = requests.get(secondUrl)
        res.raise_for_status()
        values = res.json()
    except (HTTPError, Timeout, ConnectionError, JSONDecodeError) as msg:
        sys.exit(msg)
    except requests.exceptions.RequestException as msg:
        sys.exit(msg)
    for val in values:
        theid = val.get('userId')
        uname = users.get(theid)
        title = val.get('title')
        completed = val.get('completed')
        if tasks.get(f'{theid}') is None:
            tasks[f'{theid}'] = []
        tasks[f'{theid}'].append(
            {"username": uname, 'task': title, 'completed': completed})
    with open('todo_all_employees.json', mode='w') as file:
        json.dump(tasks, file)


if __name__ == '__main__':
    export_tojson()
