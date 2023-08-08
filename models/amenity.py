#!/usr/bin/python3
""" Module that contains class Amenity """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""

    def __init__(self, *args, **my_dict):
        """ constructor """
        self.name = ""
        super().__init__(*args, **my_dict)
