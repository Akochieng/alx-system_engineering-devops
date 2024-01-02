#!/usr/bin/python3
'''
Simple module to fetch data from a remote web app and save on a json file
'''
import json
from json import JSONDecodeError
from requests.exceptions import ConnectionError, HTTPError, Timeout
from requests import exceptions
import requests
from sys import argv
import sys


def export_tojson():
    '''
    saves a user and ther to do list on a json file
    '''
    if len(argv) != 2:
        sys.exit(f"Usage: {argv[0]} employee_id")
    USER_ID = argv[1]
    userUrl = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
    secondUrl = f"https://jsonplaceholder.typicode.com/users/{USER_ID}/todos"
    tasks = []
    try:
        userInfo = requests.get(userUrl)
        userInfo.raise_for_status()
        USERNAME = userInfo.json().get('username')
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
        tasks.append({
            "task": val.get('title'), 'completed': val.get('completed'),
            'username': USERNAME})
    with open(f'{USER_ID}.json', mode='w') as file:
        json.dump({f'{USER_ID}': tasks}, file)


if __name__ == '__main__':
    export_tojson()
