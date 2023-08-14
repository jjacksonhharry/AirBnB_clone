#!/usr/bin/python3
"""Contains the unttests for filestorage.py"""
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
            print(self.storage._FileStorage__objects)
            print(self.storage._FileStorage__file_path)

    def test_reload(self):
        # Save the current state of the objects in the storage
        current_objects = self.storage.all()

        # Create a new storage instance and reload data
        storage_2 = FileStorage()
        storage_2.reload()

        # Get the reloaded objects from the new storage instance
        reloaded_objects = storage_2.all()

        # Compare the current and reloaded objects
        self.assertDictEqual(current_objects, reloaded_objects)

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

    def test_objects_initialization(self):
        # Ensure that __objects is initially empty
        self.assertEqual(len(self.storage._FileStorage__objects), 0)

    def test_new_method_updates_objects(self):
        # Test that new() method updates __objects correctly
        self.storage.new(self.obj_1)
        self.assertEqual(len(self.storage._FileStorage__objects), 1)

    def test_all_method_returns_objects(self):
        # Test that all() method returns the __objects dictionary
        all_objects = self.storage.all()
        self.assertEqual(all_objects, self.storage._FileStorage__objects)

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
