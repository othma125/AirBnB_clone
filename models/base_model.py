#!/usr/bin/python3
""" Module that contains class Base """
import sys
import time
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ Base class """

    def __init__(self):
        """ constructor """
        self.id: str = str(uuid4())
        self.created_at: datetime = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ to string """
        return f"[{self.__class__.__name__} ({self.id}) {self.__dict__}]"

    def save(self):
        self.updated_at = datetime.now()

model = BaseModel()
model.name = 'first name'
model.my_number = 98
print(model)
time.sleep(2)
model.save()
print(model)