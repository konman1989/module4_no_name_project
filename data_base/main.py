import json


class DataBase:
    def __init__(self):
        self.database = {'tables': {}, 'data': {}}
        self.field_types = {
            'int': int,
            'str': str,
            'boolean': bool}

    def add_tables(self, name: str, parameters: dict):
        if name not in self.database['tables']:
            self.database['tables'].update({name: parameters})

    def add_data(self, table_name: str, data: dict):
        keys_checked = 0
        for n in data.keys():
            if n in self.database['tables'][table_name].keys():
                if type(data[n]) == \
                        self.field_types[self.database[
                            'tables'][table_name][n]]:
                    keys_checked += 1
        if keys_checked == len(data.keys()):
            if table_name in self.database['data']:

                self.database['data'][table_name].append(data)
            else:
                self.database['data'].update({f'{table_name}': []})
                self.database['data'][table_name].append(data)

    def select(self, table: str, limit: int = None):
        with open('Database.json', 'r') as db:
            dict_list1 = json.load(db)
            dict_list = dict_list1['data'][table]
            new_list = []
            for num in dict_list:
                new_list.append(num)
            return new_list[0:limit]

    # def id_creator(self):
    #     with open('Database.json', 'r') as ids:
    #         id_json = json.load(ids)
    #         tables_list = id_json['tables']
    #         id_list = []
    #         id_ = 0
    #         for table in tables_list.values():
    #             id_list.append(table['id'])
    #         if id_list[-1] == 'int':
    #             id_ = 0
    #         else:
    #             id_ = id_list[-1] + 1
    #         print(id_)
    #         return id_

    @staticmethod
    def compare_databases(database, json_data):
        for key in database['tables'].keys():
            if key not in json_data['tables'].keys():
                json_data['tables'].update({key: database[key]})
        for key in database['data'].keys():
            if key not in json_data['data'].keys():
                json_data['data'].update({key: database[key]})
            for item in database['data'][key]:
                if item not in json_data['data'][key]:
                    json_data['data'][key].append(item)
        return json_data

    def to_json(self):
        with open('Database.json', 'r') as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                with open('Database.json', 'w') as file1:
                    json.dump(self.database, file1, indent=2)
                    return
            data = self.compare_databases(self.database, data)
            with open('Database.json', 'w') as file1:
                json.dump(data, file1, indent=2)


DB = DataBase()
DB.add_tables('Songs', {'id': 'int', 'name': 'str', 'lyrics': 'str'})
DB.add_data('Songs', {'id': 1001, 'name': 'In Bloom', 'lyrics': 'test'})
DB.add_data('Songs', {'id': 1002, 'name': 'Wild', 'lyrics': 'test'})
DB.to_json()
DB.add_data('Songs', {'id': 1003, 'name': 'Nobody', 'lyrics': 'test'})
DB.add_data('Songs', {'id': 1004, 'name': 'No Plan', 'lyrics': 'test'})
DB.to_json()
DB.add_data('Songs', {'id': 1005, 'name': 'Almost', 'lyrics': 'test'})
DB.to_json()

