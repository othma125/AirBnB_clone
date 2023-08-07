#!/usr/bin/python3
""" Module that contains class Review """
from models.base_model import BaseModel

class Review(BaseModel):
    """Review class"""

    def __init__(self, *args, **my_dict):
        """ constructor """
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(self, args, my_dict)