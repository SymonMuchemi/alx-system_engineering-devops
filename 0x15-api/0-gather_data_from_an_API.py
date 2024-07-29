#!/usr/bin/python3
"""Fetch information on employee's completed tasks"""


if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) < 2:
        exit()

    baseUrl = "https://jsonplaceholder.typicode.com"
    id = argv[1]
    name = requests.get(
        f"{baseUrl}/users?id={id}"
    )
    completed_todos = requests.get(
        f"{baseUrl}/todos?usersId={id}&completed=true"
    )
    all_todos = requests.get(
        f"{baseUrl}/todos?usersId={id}"
    )

    employee_name = name.json()[0]['name']
    done_todos = completed_todos.json()
    done = len(completed_todos.json())
    all = len(all_todos.json())

    todos_list = [f"\t{x['title']}" for x in done_todos]
    print(f"Employee {employee_name} is done with tasks({done}/{all})")

    for todo in todos_list:
        print(todo)
