#!/usr/bin/python3
"""
This is the basemodel module and it defines the BaseModel class
"""
from datetime import datetime
import uuid


class BaseModel():
    """
    This is the class BaseModel
    It defines all common attributes and methods for other classes
    """
    def __init__(self):
        """
        Initializes an instances
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a  string representation of an instance
        """
        string = "[" + self.__class__.__name__ + "] (" + str(self.id) + ") "
        return string + str(self.__dict__)

    def save(self):
        """
        Updates the public instance attibute updated_at
        with the current date time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containg all key/values of
        __dict__ instance
        """
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        obj_dict = self.__dict__
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
