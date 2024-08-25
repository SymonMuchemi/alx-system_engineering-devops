#!/usr/bin/python3
"""
place holder
"""
import csv
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

    return user_data[0]['username'] if user_data else None


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


def get_data_for_csv(base_url, user_id):
    """create dict to add to csv

    Args:
        base_url (str): path to data
        user_id (int): user's id

    Returns:
        list: tasks data
    """
    url = f'{base_url}/todos?userId={user_id}'
    user_name = get_username(base_url, user_id)

    data = fetch_data(url)
    data_list = []

    for item in data:
        item = dict(
            USER_ID=user_id,
            USERNAME=user_name,
            TASK_COMPLETED_STATUS=item['completed'],
            TASK_TITLE=item['title']
        )
        data_list.append(item)

    return data_list


def write_to_csv(base_url, user_id):
    file_name = f'{user_id}.csv'
    data = get_data_for_csv(base_url, user_id)

    fields = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open(file_name, mode='w+', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        # writer.writeheader()

        writer.writerows(data)


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

    write_to_csv(base_url, user_id)
