#!/usr/bin/python3
"""
use the url to returns information about employee
"""
import json
import requests


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as f:
        json.dump({
            e.get("id"): [{
                "task": r.get("title"),
                "completed": r.get("completed"),
                "username": e.get("username")
            } for r in requests.get(url + "todos",
                                    params={"userId": e.get("id")}).json()]
            for e in users}, f)
