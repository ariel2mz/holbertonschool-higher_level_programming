#!/usr/bin/python3
"""
Este script obtiene posts desde una API y los guarda en un archivo CSV.
"""
import requests
import csv

# Función para obtener y mostrar los posts
def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    codigo = r.status_code
    print(f"Status Code: {codigo}")
    
    if codigo == 200:
        info = r.json()
        for post in info:
            print(f"ID: {post.get('id')}, Título: {post.get('title')}")

# Función para obtener y guardar los posts en un archivo CSV
def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    codigo = r.status_code
    print(f"Status Code: {codigo}")
    
    if codigo == 200:
        lista = []
        info = r.json()
        
        for post in info:
            post_dict = {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            lista.append(post_dict)
        
        # Guardar la lista en un archivo CSV
        csv_file = 'posts.csv'
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            
            # Escribir la cabecera (los nombres de las columnas)
            writer.writeheader()
            
            # Escribir las filas (cada post)
            writer.writerows(lista)
        