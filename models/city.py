#!/usr/bin/python3
""" Module that contains class City """
from models.base_model import BaseModel


class City(BaseModel):
    """City class"""

    def __init__(self, *args, **my_dict):
        """ constructor """
        self.state_id = ""
        self.name = ""
        super().__init__(args, my_dict)
