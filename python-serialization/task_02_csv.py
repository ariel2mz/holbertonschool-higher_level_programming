import csv 
import json

def convert_csv_to_json(filename):
    
    try:
        with open(filename, 'r') as file:
            aux = csv.DictReader(file)
            aux = list(aux)
        with open('data.json', 'w') as file:
            json.dump(aux, file, indent=4)

        return True
    except FileNotFoundError:
        return False
    except EOFError:
        return  False