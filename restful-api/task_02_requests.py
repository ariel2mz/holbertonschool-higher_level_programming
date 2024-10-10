#!/usr/bin/python3
"""
adssada
"""


def fetch_and_print_posts():
    r = r.get('https://jsonplaceholder.typicode.com/')
    codigo = r.status_code
    printf(f"{codigo}")
    if codigo == 200:
        info = r.json()
        for key, value in json_data.items():
            print(f"{key}")