#!/usr/bin/python3
import unittest
import os
import json

from models.base_model import BaseModel
from models.place import Place
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    def setUp(self):
        self.place = Place()
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_state_instatnce(self):
        self.assertTrue(isinstance(self.place, BaseModel))
        new_place = Place()
        self.assertEqual(type(self.place), type(new_place))

    def test_attributes_exists(self):
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))

    def test_with_kwargs(self):
        obj = self.storage.all()
        new_place = Place(**obj)
        self.assertNotEqual(self.place, new_place)
        self.assertEqual(self.place.name, new_place.name)

    def test_serialization(self):
        self.place.save()
        with open('file.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        key = '{}.{}'.format('Place', self.place.id)
        self.assertIn(key, data)

    def test_deserialization(self):
        self.place.save()
        obj1 = self.storage.all()
        store = FileStorage()
        store.reload()
        obj2 = store.all()
        self.assertEqual(obj1, obj2)


if __name__ == '__main__':
    unittest.main()
