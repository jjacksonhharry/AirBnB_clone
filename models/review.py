#!/usr/bin/python3
# This is the review module defining a class Review
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class representing reviews
    """
    place_id = ""
    user_id = ""
    text = ""
