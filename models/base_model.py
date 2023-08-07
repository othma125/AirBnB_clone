#!/usr/bin/python3
""" Module that contains class BaseModel """

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Base class"""

    def __init__(self, *args, **kwargs):
        """
        constructor
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        """
        from models import storage

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    t = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, t)
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id: str = str(uuid4())
            self.created_at: datetime = datetime.now()
            self.updated_at: datetime = self.created_at
        storage.new(self)
        storage.save()

    def __str__(self) -> str:
        """to string"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """ update """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self) -> dict:
        """return dic"""
        my_dict = self.__dict__.copy()
        my_dict.update({"__class__": self.__class__.__name__})
        my_dict.update({"created_at": str(self.created_at.isoformat())})
        my_dict.update({"updated_at": str(self.updated_at.isoformat())})
        return my_dict
