#!/usr/bin/python3
"""This module defines the FileStorage class"""
import json
import os
import datetime


class FileStorage():
    """
    Serializez instances to a JSON file and also
    Deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(new):
        """
        Returns a dictionary stored in __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <classname.id>
        """
        class_name = obj.__class__.__name__
        id = obj.id
        key = f"{class_name}.{id}"
        FileStorage.__objects[key] = obj

    def import_class(self):
        """
        Imports needed class names
        Returns a dictionary with the needed classes
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        return {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }

    def save(self):
        """
        Serializes __objects to the json file
        """
        json_dictionary = {}
        for key, obj in FileStorage.__objects.items():
            json_dictionary[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(json_dictionary, file)

    def reload(self):
        """
        deserializes the json file to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)
                for key, json_dict in json_data.items():
                    class_name, obj_id = key.split('.')
                    new_instance = self.import_class()[class_name](**json_dict)
                    FileStorage.__objects[key] = new_instance
