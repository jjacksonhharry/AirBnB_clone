#!/usr/bin/python3
"""unittests for models/state.py"""
import unittest
import os
import json

from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_state_instatnce(self):
        self.assertTrue(isinstance(self.state, BaseModel))
        state2 = State()
        self.assertEqual(type(self.state), type(state2))

    def test_attributes_exists(self):
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))

    def test_with_kwargs(self):
        obj = self.storage.all()
        new_state = State(**obj)
        self.assertNotEqual(self.state, new_state)
        self.assertEqual(self.state.name, new_state.name)

    def test_serialization(self):
        self.state.save()
        with open('file.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        key = '{}.{}'.format('State', self.state.id)
        self.assertIn(key, data)

    def test_deserialization(self):
        self.state.save()
        obj1 = self.storage.all()
        store = FileStorage()
        store.reload()
        obj2 = store.all()
        self.assertEqual(obj1, obj2)


if __name__ == '__main__':
    unittest.main()
