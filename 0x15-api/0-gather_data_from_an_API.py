#!/usr/bin/python3
"""
place holder
"""
import requests
from sys import argv


def fetch_data(url):
    """get data from url

    Args:
        url (str): path

    Returns:
        dict: response in json format
    """
    response = requests.get(url)
    return response.json()


def get_username(base_url, user_id):
    """get the username

    Args:
        base_url (str): path to user data
        user_id (int): the user's id

    Returns:
        str: the name of the user
    """
    url = f'{base_url}/users?id={user_id}'
    user_data = fetch_data(url)

    return user_data[0]['name'] if user_data else None


def get_completed_tasks(base_url, user_id):
    """get all tasks completed by the user

    Args:
        base_url (str): path to user data
        user_id (int): user's id

    Returns:
        dict: response in json format
    """
    url = f'{base_url}/todos?userId={user_id}&completed=true'
    return fetch_data(url)


def get_tasks(base_url, user_id):
    """fetch user tasks data

    Args:
        base_url (str): path to tasks data
        user_id (int): user's id

    Returns:
        dict: json format response
    """
    url = f'{base_url}/todos?userId={user_id}'
    
    return fetch_data(url)


def get_total_task_count(base_url, user_id):
    """get the total number of tasks done by a user

    Args:
        base_url (str): path to user dat
        user_id (int): the user's id

    Returns:
        int: number of completed tasks
    """
    url = f'{base_url}/todos?userId={user_id}'
    all_tasks = fetch_data(url)

    return len(all_tasks)


def print_task_summary(name, completed_tasks, total_tasks):
    """print a summary of a user's completed tasks

    Args:
        name (str): name of the user
        completed_tasks (dict): tasks completed data
        total_tasks (int): number of completed tasks
    """
    completed_len = len(completed_tasks)
    todo_list = []

    for task in completed_tasks:
        todo_list.append(task['title'])
    print(f'Employee {name} is done with tasks({completed_len}/{total_tasks})')
    for task in todo_list:
        print(f'\t{task}')


if __name__ == "__main__":
    if len(argv) < 2:
        exit()

    base_url = 'https://jsonplaceholder.typicode.com'
    user_id = argv[1]

    name = get_username(base_url, user_id)
    if not name:
        print('User not found')
        exit()

    completed_tasks = get_completed_tasks(base_url, user_id)
    total_tasks = get_total_task_count(base_url, user_id)

    print_task_summary(name, completed_tasks, total_tasks)
