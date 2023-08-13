#!/usr/bin/python3
import json
import os
import unittest

from models.base_model import BaseModel
from models.user import User
from models import storage
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def tearDown(self):
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_user_instances(self):
        user2 = User()
        self.assertTrue(isinstance(user2, BaseModel))
        self.assertEqual(type(self.user), type(user2))

    def test_attributes_exists(self):
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))

    def test_instant_with_kwargs(self):
        objects = storage.all()
        new_user = User(**objects)
        self.assertEqual(self.user.email, new_user.email)

    def test_serialization(self):
        self.user.save()
        with open('file.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        key = '{}.{}'.format('User', self.user.id)
        self.assertIn(key, data)

    def test_deserialization(self):
        self.user.save()
        object1 = storage.all()
        store = FileStorage()
        store.reload()
        object2 = store.all()
        self.assertEqual(object1, object2)


if __name__ == '__main__':
    unittest.main()
