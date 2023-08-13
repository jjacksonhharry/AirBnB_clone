#!/usr/bin/python3
# This is is the user module that defines the User class
from models.base_model import BaseModel
from . import storage


class User(BaseModel):
    """
    class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
