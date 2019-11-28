import unittest
import json
from main import DataBase
import os


class TestDataBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.db = DataBase()
        with open('Database.json', 'w') as file1:
            json.dump(cls.db.database, file1, indent=2)

    def setUp(self) -> None:
        self.field_types = self.db.add_tables('Songs', {
            'id': 'int', 'name': 'str', 'lyrics': 'str'})
        self.data = self.db.add_data('Songs', {'id': 0, 'name': 'In Bloom',
                                               'lyrics': 'test'})

    def tearDown(self) -> None:
        os.remove('Database.json')

    def test_add_tables(self):
        self.field_types = self.db.add_tables('Songs', {
            'id': 'int', 'name': 'str', 'lyrics': 'str'})
        with open('Database.json', 'r') as file1:
            tables = json.load(file1)
            self.assertTrue(tables)
            self.assertIn('tables', tables)
            table_key = ['id', 'name', 'lyrics']
            table_value = ['int', 'str', 'str']
            keys = []
            values = []
            for key, value in tables['tables']['Songs'].items():
                keys.append(key)
                values.append(value)
            self.assertEqual(table_key, keys)
            self.assertEqual(table_value, values)

    def test_add_data(self):
        self.data = self.db.add_data('Songs', {'id': 0, 'name': 'In Bloom',
                                               'lyrics': 'test'})
        with open('Database.json', 'r') as file1:
            data_ = json.load(file1)
            self.assertTrue(data_)
            self.assertIn('data', data_)
            data_key = ['id', 'name', 'lyrics']
            data_value = [0, 'In Bloom', 'test']
            keys = []
            values = []
            for data_list in data_['data']['Songs']:
                for key, value in data_list.items():
                    keys.append(key)
                    values.append(value)
            self.assertEqual(data_key, keys)
            self.assertEqual(data_value, values)

    def test_select(self):
        self.db.select('Songs', name='In Bloom', lyrics='test')
        select_object = [{'id': 0, 'name': 'In Bloom', 'lyrics': 'test'}]
        select_keys = []
        select_values = []
        for select_list in select_object:
            for key, value in select_list.items():
                select_keys.append(key)
                select_values.append(value)

        with open('Database.json', 'r') as file1:
            data_select = json.load(file1)
            keys = []
            values = []
            for data_list in data_select['data']['Songs']:
                for key, value in data_list.items():
                    keys.append(key)
                    values.append(value)
            self.assertEqual(select_keys, keys)
            self.assertEqual(select_values, values)

    def test_to_json(self):
        with open('Database.json', 'r') as file1:
            self.assertIsNotNone(file1)
