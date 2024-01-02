#!/usr/bin/env python3
'''
A simple module to fetch data from remote webapp and save
the data on a csv file.
'''
import csv
from json import JSONDecodeError
import requests
from requests import exceptions
from requests.exceptions import HTTPError, Timeout, ConnectionError
from sys import argv
import sys


def export_tocsv():
    '''
    fetches employee id and todo lists and saves it on a csv file.
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
    with open(f'{USER_ID}.csv', mode='w') as file:
        csvwriter = csv.writer(
            file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for val in values:
            csvwriter.writerow(
                [USER_ID, USERNAME, val.get('completed'), val.get('title')])


if __name__ == '__main__':
    export_tocsv()
