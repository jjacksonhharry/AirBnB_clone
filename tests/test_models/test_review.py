#!/usr/bin/python3
"""unittests for models/review"""
import unittest
import os
import json

from models.base_model import BaseModel
from models.review import Review
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    def setUp(self):
        self.review = Review()
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_state_instatnce(self):
        self.assertTrue(isinstance(self.review, BaseModel))
        new_review = Review()
        self.assertEqual(type(self.review), type(new_review))

    def test_attributes_exists(self):
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))

    def test_with_kwargs(self):
        obj = self.storage.all()
        new_review = Review(**obj)
        self.assertNotEqual(self.review, new_review)
        self.assertEqual(self.review.text, new_review.text)

    def test_serialization(self):
        self.review.save()
        with open('file.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        key = '{}.{}'.format('Review', self.review.id)
        self.assertIn(key, data)

    def test_deserialization(self):
        self.review.save()
        obj1 = self.storage.all()
        store = FileStorage()
        store.reload()
        obj2 = store.all()
        self.assertEqual(obj1, obj2)


if __name__ == '__main__':
    unittest.main()
