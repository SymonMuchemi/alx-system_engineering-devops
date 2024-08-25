#!/usr/bin/python3
"""
place holder
"""
import requests
from sys import argv

def fetch_data(url):
    response = requests.get(url)
    return response.json()

def get_username(base_url, user_id):
    url = f'{base_url}/users?id={user_id}'
    user_data = fetch_data(url)
    
    return user_data[0]['name'] if user_data else None

def get_completed_tasks(base_url, user_id):
    url = f'{base_url}/todos?userId={user_id}&completed=true'
    return fetch_data(url)

def get_total_task_count(base_url, user_id):
    url = f'{base_url}/todos?userId={user_id}'
    all_tasks = fetch_data(url)
    
    return len(all_tasks)

def print_task_summary(name, completed_tasks, total_tasks):
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
