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
        self.updated_at = self.created_at

    def __str__(self):
        return f"[{self.__class__.__name__} ({self.id}) {self.__dict__}]"
