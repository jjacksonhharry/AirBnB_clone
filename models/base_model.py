#!/usr/bin/python3
"""
This is the basemodel module and it defines the BaseModel class
"""
import uuid
from datetime import datetime
from . import storage


class BaseModel():
    """
    This is the class BaseModel
    It defines all common attributes and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes an instances
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a  string representation of an instance
        """
        string = "[" + self.__class__.__name__ + "] (" + self.id + ") "
        return string + str(self.__dict__)

    def save(self):
        """
        Updates the public instance attibute updated_at
        with the current date time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containg all key/values of
        __dict__ instance
        """
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
