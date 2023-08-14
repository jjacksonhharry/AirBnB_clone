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

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_place_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    def test_user_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def test_text_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    def test_two_reviews_unique_ids(self):
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    def test_args_unused(self):
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

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

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        rv = Review()
        self.assertIn("id", rv.to_dict())
        self.assertIn("created_at", rv.to_dict())
        self.assertIn("updated_at", rv.to_dict())
        self.assertIn("__class__", rv.to_dict())

    def test_to_dict_contains_added_attributes(self):
        rv = Review()
        rv.middle_name = "Holberton"
        rv.my_number = 98
        self.assertEqual("Holberton", rv.middle_name)
        self.assertIn("my_number", rv.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        rv = Review()
        rv_dict = rv.to_dict()
        self.assertEqual(str, type(rv_dict["id"]))
        self.assertEqual(str, type(rv_dict["created_at"]))
        self.assertEqual(str, type(rv_dict["updated_at"]))

    def test_contrast_to_dict_dunder_dict(self):
        rv = Review()
        self.assertNotEqual(rv.to_dict(), rv.__dict__)

    def test_to_dict_with_arg(self):
        rv = Review()
        with self.assertRaises(TypeError):
            rv.to_dict(None)


if __name__ == '__main__':
    unittest.main()
