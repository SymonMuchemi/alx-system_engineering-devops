#!/usr/bin/python3
"""
place holder
"""


if __name__ == "__main__":

    import requests
    from sys import argv
    if len(argv) < 2:
        exit()
    baseUrl = "https://jsonplaceholder.typicode.com"
    todos = requests.get(
        "{}/todos?userId={}&completed=true"
        .format(baseUrl, argv[1]))
    name = requests.get(
        "{}/users?id={}"
        .format(baseUrl, argv[1]))
    name = name.json()
    name = name[0]["name"]
    todo = requests.get(
        "{}/todos?userId={}".format(baseUrl, argv[1]))
    todo = todo.json()
    todo = len(todo)
    todos = todos.json()
    todo_list = []

    for x in todos:
        todo_list.append("\t {}".format(x["title"]))
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(todos), todo))
    for y in todo_list:
        print(y)
