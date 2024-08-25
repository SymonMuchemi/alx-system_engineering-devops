#!/usr/bin/python3
"""
place holder
"""
import json
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


def get_employee_ids(base_url):
    """gets a list of all employee ids

    Args:
        base_url (str): path to data

    Returns:
        list: list of employee ids
    """
    url = f'{base_url}/users/'
    employees_data = fetch_data(url)

    # print(type(employees_data))
    # print(employees_data)

    employee_ids = []

    for employee in employees_data:
        id = employee.get('id')
        if id not in employee_ids:
            employee_ids.append(id)

    return employee_ids


def prep_employee_data(base_url, user_id):
    """create dict to add to json file

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
            task=item['title'],
            completed=item['completed'],
            username=user_name,
        )
        data_list.append(item)

    return data_list


def write_to_json(base_url, list_of_ids):
    """writes data to a json file

    Args:
        base_url (str): path to data
        list_of_ids (list): list of user ids
    """
    file_name = 'todo_all_employees.json'

    data_dict = {}

    for id in list_of_ids:
        data_dict[id] = prep_employee_data(base_url, id)

    with open(file_name, 'a') as file:
        json.dump(data_dict, file)


if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com'

    ids_list = get_employee_ids(base_url)

    write_to_json(base_url, ids_list)
    # print_task_summary(name, completed_tasks, total_tasks)
