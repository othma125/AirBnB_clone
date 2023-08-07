#!/usr/bin/python3
""" Module that contains class State """
from models.base_model import BaseModel


class State(BaseModel):
    """State class"""

    def __init__(self, *args, **my_dict):
        """ constructor """
        self.name = ""
        super().__init__(self, args, my_dict)
