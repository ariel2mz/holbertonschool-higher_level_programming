import csv 
import json

def convert_csv_to_json(filename):
    with open(filename, 'r') as file:
        aux = csv.DictReader(file)
    
    serial = json.dump(aux)
    try:
        with open('data.json', 'w') as file:
            file = json.dump(serial)
        return True
    except FileNotFoundError:
        return False
    except EOFError:
        return  False