#!/usr/bin/python3
"""
use the url, for a given employee ID, returns information about his todos
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    id = argv[1]

    user = requests.get(url + "{}".format(id)).json()

    todos = requests.get(url + "{}/todos".format(id)).json()

    with open("{}.json".format(id), "w") as f:
        json.dump({id: [{
                "task": elem.get("title"),
                "completed": elem.get("completed"),
                "username": user.get("username")
            } for elem in todos]}, f)
