#!/usr/bin/python3
""" Module that contains class Base """

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ Base class """

    def __init__(self):
        """ constructor """
        self.id: str = str(uuid4())
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = self.created_at

    def __str__(self):
        """ to string """
        return f"[{self.__class__.__name__} ({self.id}) {self.__dict__}]"

    def save(self):
        """ update """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ return dic """
        dict = self.__dict__.copy()
        dict['__class__']: str = self.__class__.__name__
        dict['created_at']: str = str(self.created_at.isoformat())
        dict['updated_at']: str = str(self.updated_at.isoformat())
        return dict

model = BaseModel()
model.name:str = 'first name'
model.my_number = 98
print(model)
model.save()
tojson = model.to_dict()
print(tojson)
for key in tojson.keys():
    print(f'{key} {type(tojson[key])}')