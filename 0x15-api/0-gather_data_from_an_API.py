#!/usr/bin/python3
"""
use the url, for a given employee ID, returns information about his todos
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    id = argv[1]

    user = requests.get(url + "{}".format(id)).json()

    todos = requests.get(url + "{}/todos".format(id)).json()

    infos = [c.get("title") for c in todos if c.get("completed") is True]
    text = "Employee {} is done with tasks({}/{}):"

    print(text.format(user.get("name"), len(infos), len(todos)))
    [print(f"\t {elem}") for elem in infos]
