#!/usr/bin/python3
import unittest
import os
import json

from models.base_model import BaseModel
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_state_instatnce(self):
        self.assertTrue(isinstance(self.amenity, BaseModel))
        amenity2 = Amenity()
        self.assertEqual(type(self.amenity), type(amenity2))

    def test_attributes_exists(self):
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))

    def test_with_kwargs(self):
        obj = self.storage.all()
        new_amenity = Amenity(**obj)
        self.assertNotEqual(self.amenity, new_amenity)
        self.assertEqual(self.amenity.name, new_amenity.name)

    def test_serialization(self):
        self.amenity.save()
        with open('file.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        key = '{}.{}'.format('Amenity', self.amenity.id)
        self.assertIn(key, data)

    def test_deserialization(self):
        self.amenity.save()
        obj1 = self.storage.all()
        store = FileStorage()
        store.reload()
        obj2 = store.all()
        self.assertEqual(obj1, obj2)


if __name__ == '__main__':
    unittest.main()
