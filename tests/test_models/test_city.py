#!/usr/bin/python3
"""unittests for models/city.py"""
import unittest
import os
import json

from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    def setUp(self):
        self.city = City()
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_state_instatnce(self):
        self.assertTrue(isinstance(self.city, BaseModel))
        city2 = City()
        self.assertEqual(type(self.city), type(city2))

    def test_attributes_exists(self):
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))

    def test_with_kwargs(self):
        obj = self.storage.all()
        new_city = City(**obj)
        self.assertNotEqual(self.city, new_city)
        self.assertEqual(self.city.name, new_city.name)

    def test_serialization(self):
        self.city.save()
        with open('file.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        key = '{}.{}'.format('City', self.city.id)
        self.assertIn(key, data)

    def test_deserialization(self):
        self.city.save()
        obj1 = self.storage.all()
        store = FileStorage()
        store.reload()
        obj2 = store.all()
        self.assertEqual(obj1, obj2)


if __name__ == '__main__':
    unittest.main()
