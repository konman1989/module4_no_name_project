import os
import json


class DataBase:
    def __init__(self):
        self.field_types = {
            'int': int,
            'str': str,
            'boolean': bool}

    @property
    def database(self):
        if not os.path.exists('Database.json'):
            file = open('Database.json', 'w')
            file.close()
        with open('Database.json', 'r') as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                data = {'tables': {}, 'data': {}}
            return data

    def id_creator(self, table_name):
        try:
            table_contents = self.database['data'][table_name]
            return table_contents[-1]['id'] + 1
        except KeyError:
            return 0

    def add_tables(self, name: str, parameters: dict):
        data = self.database
        if name not in data['tables']:
            data['tables'].update({name: parameters})
        self.to_json(data)

    def add_data(self, table_name: str, parameters: dict):
        data = self.database
        keys_checked = 0
        for n in parameters:
            if n in data['tables'][table_name]:
                if type(parameters[n]) == \
                        self.field_types[data[
                            'tables'][table_name][n]]:
                    keys_checked += 1
        if keys_checked == len(parameters):
            try:
                objects = [n['name'] for n in self.database['data'][table_name]]
            except KeyError:
                objects = []
            if parameters['name'] not in objects:
                if table_name in data['data']:
                    parameters = {'id': self.id_creator(table_name), **parameters}
                    data['data'][table_name].append(parameters)
                else:
                    data['data'].update({f'{table_name}': []})
                    parameters = {'id': self.id_creator(table_name), **parameters}
                    data['data'][table_name].append(parameters)
        self.to_json(data)

    @staticmethod
    def select(table: str, limit: int = None, **filters):
        with open('Database.json', 'r') as db:
            dict_list = json.load(db)['data'][table]
            new_list = []
            for el in dict_list:
                if filters == {}:
                    new_list.append(el)
                for fil in filters.items():
                    if fil[1] != el[fil[0]]:
                        break
                    elif el not in new_list:
                        new_list.append(el)
            if limit is None:
                return new_list
            else:
                return new_list[0:limit]

    def to_json(self, data):
        with open('Database.json', 'w') as file1:
            json.dump(data, file1, indent=2)


if __name__ == "__main__":
    DB = DataBase()
    DB.add_tables('Songs', {'id': 'int', 'name': 'str', 'lyrics': 'str'})
    DB.add_data('Songs', {'name': 'Nobody', 'lyrics': 'test'})
    DB.add_data('Songs', {'name': 'No Plan', 'lyrics': 'test'})
    DB.add_data('Songs', {'name': 'Almost', 'lyrics': 'test'})
    DB.add_data('Songs', {'name': 'Jackie and Wilson', 'lyrics': 'test'})
    DB.add_data('Songs', {'name': 'Cherry Wine', 'lyrics': 'test'})
    DB.add_data('Songs', {'name': 'R U Mine?', 'lyrics': 'test'})
    print(DB.select('Songs', name='Cherry Wine', lyrics='test'))
