from CLI import get_arg
import json


def get_data():

    name_city, vacancie= get_arg()

    with open(r'storage\only_city.json', 'r', encoding='utf-8') as f:
        cities = json.load(f)
    
    for city in cities:
        if name_city in city.get('name'):
            return city.get('id'), vacancie
    
    