import unittest
import os
import uuid

from unittest.mock import patch
from datetime import datetime, timedelta
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        pass

    def test_attributes_existence(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_is_uuid(self):
        self.assertTrue(isinstance(self.base_model.id, str))
        try:
            uuid.UUID(self.base_model.id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID")

    def test_created_at(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_method(self):
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, original_updated_at)

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__

        # Convert created_at and updated_at to ISO format strings
        if isinstance(self.created_at, datetime):
            obj_dict['created_at'] = self.created_at.isoformat()
        if isinstance(self.updated_at, datetime):
            obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict

    def test_str_method(self):
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    @patch('models.base_model.storage')
    def test_init_with_kwargs(self, mock_storage):
        kwargs = {
            'id': 'some_id',
            'created_at': '2023-08-09T06:23:27.276770',
            'updated_at': '2023-08-09T06:23:27.276770',
            'name': 'My_Model',
            '__class__': 'BaseModel'
        }
        new_model = BaseModel(**kwargs)

        self.assertEqual(new_model.id, 'some_id')
        self.assertEqual(new_model.name, 'My_Model')

if __name__ == '__main__':
    unittest.main()
