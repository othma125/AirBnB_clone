#!/usr/bin/python3
""" Module that contains class Base """
from uuid import uuid4


class BaseModel:
    """ Base class """

    def __init__(self, identifier=None):
        """ constructor """
        self.id = str(uuid4())
        # self.created_at = now
