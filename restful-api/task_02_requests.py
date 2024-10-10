#!/usr/bin/python3
"""
adssada
"""

r = requests.get('https://jsonplaceholder.typicode.com/')
codigo = r.status_code
printf(f"{codigo}")

def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/')
    codigo = r.status_code
    printf(f"{codigo}")
    if codigo == 200:
        info = r.json()
        for key, value in json_data.items():
            print(f"{key}")