#!/usr/bin/python3
""" Module that contains class User """
from models.base_model import BaseModel


class User(BaseModel):
    """User class"""

    # def __init__(self, *args, **my_dict):
    #     """ constructor """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
    # super().__init__(*args, **my_dict)
