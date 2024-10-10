#!/usr/bin/python3
"""
adssada
"""
import requests

def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/')
    codigo = r.status_code
    printf(f"{codigo}")
    if codigo == 200:
        info = r.json()
        for key, value in json_data.items():
            print(f"{key}")

def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/')
    codigo = r.status_code
    printf(f"{codigo}")
    if codigo == 200:
        lista = []
        info = r.json()
        for x in info:
            post_dict = {
            "id": post.get("id"),
            "title": post.get("title"),
            "body": post.get("body")
        }
        posts_list.append(post_dict)