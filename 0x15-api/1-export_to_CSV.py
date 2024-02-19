#!/usr/bin/python3
"""
use the url, for a given employee ID, returns information about his todos
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    id = argv[1]

    user = requests.get(url + "{}".format(id)).json()

    todos = requests.get(url + "{}/todos".format(id)).json()

    with open("{}.csv".format(id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [id, user.get("username"),
                elem.get("completed"), elem.get("title")]) for elem in todos]
