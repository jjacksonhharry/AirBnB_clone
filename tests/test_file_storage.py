#!/usr/bin/python3
import unittest
import json
import os

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all_method_returns_dictionary(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_private_attr(self):
        with self.assertRaises(AttributeError):
            print(self.storage.__objects)
            print(self.storage.__file_path)

    def test_new_method(self):
        base_model = BaseModel()
        self.storage.new(base_model)
        all_objects = self.storage.all()
        obj_key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertIn(obj_key, all_objects)

    def test_save(self):
        obj_1 = BaseModel()
        self.storage.save()
        with open('file.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        key = "{}.{}".format("BaseModel", obj_1.id)
        self.assertIn(key, data)

    def test_reload(self):
        obj_1 = BaseModel()
        self.storage.save()
        storage_2 = FileStorage()
        storage_2.reload()
        objects_1 = self.storage.all()
        objects_2 = storage_2.all()
        self.assertEqual(type(objects_1), type(objects_2))
        self.assertEqual(self.storage.all(), storage_2.all())


if __name__ == '__main__':
    unittest.main()
