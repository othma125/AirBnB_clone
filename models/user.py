#!/usr/bin/python3
""" Module that contains class User """
from models.base_model import BaseModel


class User(BaseModel):
    """User class"""

    def __init__(self, *args, **my_dict):
        """ constructor """
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(args, my_dict)
