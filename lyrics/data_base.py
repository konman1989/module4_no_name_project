import json
import lyrics

class DataBase:
    def __init__(self):
        self.database = {'tables': {}, 'data': {}}
        self.field_types = {
            'int': int,
            'str': str,
            'boolean': bool}

    def add_tables(self, table):
        self.database['tables'].update(table)

    def add_data(self, table_name: str, data: dict):
        for n in data.keys():
            if n in self.database['tables'][table_name].keys():
                if type(data[n]) == \
                        self.field_types[self.database[
                            'tables'][table_name][n]]:
                    if table_name in self.database['data']:
                        self.database['data'][table_name].append(data)
                    else:
                        self.database['data'].update({f'{table_name}': []})
                        self.database['data'][table_name].append(data)

    def to_json(self):
        with open('Database.json', 'a') as file:
            json.dump(self.database, file, indent=2)



class Table:
    def __init__(self, name: str, db: DataBase):
        self.parameters = {'id': 'int'}
        self.name = name
        self.table = {}
        self.database = db

    def add_parameter(self, name, name_type):
        if name not in self.parameters:
            self.parameters.update({name: name_type})
            self.add_to_table()

    def add_to_table(self):
        self.table.update({self.name: self.parameters})
        self.database.add_tables(self.table)


if __name__ == "__main__":
    DB = DataBase()

    t1 = Table('Users', DB)
    t1.add_parameter('name', 'str')
    t1.add_parameter('age', 'int')

    t2 = Table('Songs', DB)
    t2.add_parameter('artist', 'str')
    t2.add_parameter('name', 'str')
    t2.add_parameter('lyrics', 'str')

    DB.add_data('Songs', {"id": 1001, "artist": "Nirvana", "name": "In Bloom", "lyrics": "Text"})


    DB.add_data('Users', {'name': 'Steve'})
    # print(DB.database)

    DB.to_json()

