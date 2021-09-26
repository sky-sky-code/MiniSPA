import json

from sqlalchemy import text
from server.app.db.database import Session
from server.app.db.models import SingleTable

from server import config

import datetime as dt

session = Session()


def _add_data():
    st = session.query(SingleTable).all()
    if len(st) == 0:
        with open(f'{config.server_dir}\\single_data.json', 'r', encoding='utf8') as file:
            src = json.load(file)

        for item in src:
            id = item['id']
            date_one = item['date_departure']
            name = item['name_city']
            quantity = item['quantity_human']
            distance = item['distance']
            add_table = SingleTable(id=id, date_departure=dt.datetime.strptime(date_one, '%Y-%m-%d').date(),
                                    name_city=name,
                                    quantity_human=quantity, distance=distance)
            session.add(add_table)
            session.commit()

def all_data():
    data_rest = []
    data_table = session.query(SingleTable).all()
    for item in data_table:
        data_rest.append(
            {
                'id': item.id,
                'data_departure': item.date_departure,
                'name_city': item.name_city,
                'quantity_human': item.quantity_human,
                'distance': item.distance
            }
        )
    return data_rest

def _helper(help_comparison, comparison):
    data_rest = []
    for keys, value in help_comparison.items():
        if keys == comparison:
            for item in session.query(SingleTable).filter(text(value)):
                data_rest.append(
                    {
                        'id': item.id,
                        'data_departure': item.date_departure,
                        'name_city': item.name_city,
                        'quantity_human': item.quantity_human,
                        'distance': item.distance
                    }
                )
        break
    return data_rest

def filter_data(column, comparison, data_input):
    if data_input.isalpha():
        help_comparison = {
            'содержит': f"{column} LIKE '%{data_input}%'"
        }
        return _helper(help_comparison, comparison)
    elif data_input.isdigit():
        help_comparison = {
            '>': f'{column} > {int(data_input)}',
            '<': f'{column} < {int(data_input)}',
            '=': f'{column} = {int(data_input)}',
        }
        return _helper(help_comparison, comparison)


print(filter_data('name_city', 'содержит', 'Токио'))