#!/usr/bin/python3
'''
A simple python API to extract to do list of an employee from the
json place holder test webapp
'''
from json import JSONDecodeError
from requests import exceptions
from requests.exceptions import ConnectionError, HTTPError, Timeout
import requests
from sys import argv
import sys


def print_todo():
    '''
    A simple function to fetch employee details and their to do list
    from a remote webapp and print them on the terminal.
    '''
    if len(argv) != 2:
        sys.exit(f"Usage: {argv[0]} employee_id")
    userUrl = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    secondUrl = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    completed = []
    try:
        userInfo = requests.get(userUrl)
        userInfo.raise_for_status()
        EMPLOYEE_NAME = userInfo.json().get('name')
    except (HTTPError, Timeout, ConnectionError, JSONDecodeError) as msg:
        sys.exit(msg)
    except requests.exceptions.RequestException as msg:
        sys.exit(msg)
    try:
        res = requests.get(secondUrl)
        res.raise_for_status()
        values = res.json()
        TOTAL_NUMBER_OF_TASKS = len(values)
        for val in values:
            if (val.get('completed') is True):
                NUMBER_OF_DONE_TASKS += 1
                completed.append(val.get('title'))
        print(
            f"Employee {EMPLOYEE_NAME} is done with tasks("
            f"{NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
        for item in completed:
            print(f"\t {item}")
    except (HTTPError, Timeout, ConnectionError, JSONDecodeError) as msg:
        print(msg)
    except requests.exceptions.RequestException as msg:
        sys.exit(msg)


if __name__ == '__main__':
    print_todo()
