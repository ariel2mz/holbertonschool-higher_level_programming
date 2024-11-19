import csv 
import json

def convert_csv_to_json(filename):
    
    try:
        with open(filename, 'wr') as file:
            aux = csv.DictReader(file)
            json.dump('data.json', aux)
        return True
    except FileNotFoundError:
        return False
    except EOFError:
        return  False