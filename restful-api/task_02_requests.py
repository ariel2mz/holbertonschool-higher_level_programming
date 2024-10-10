#!/usr/bin/python3
"""
adssada
"""

r = requests.get('https://jsonplaceholder.typicode.com/')
codigo = r.status_code
printf(f"{codigo}")