#!/usr/bin/python3
# This module defines the City class

from models.base_model import BaseModel


class City(BaseModel):
    """
    class representing cities
    """
    state_id = ""
    name = ""
