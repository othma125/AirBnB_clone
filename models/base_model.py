#!/usr/bin/python3
""" Module that contains class BaseModel """

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ Base class """

    def __init__(self, *args, ** my_dict):
        """
        constructor
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        """
        if my_dict:
            for key, value in my_dict.items():
                if key == 'created_at' or key == 'updated_at':
                    t = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, t)
                elif key == '__class__':
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id: str = str(uuid4())
            self.created_at: datetime = datetime.now()
            self.updated_at: datetime = self.created_at
        storage.new(self)

    def __str__(self) -> str:
        """ to string """
        return f"[{self.__class__.__name__} ({self.id}) {self.__dict__}]"

    def save(self) -> None:
        """ update """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """ return dic """
        my_dict = self.__dict__.copy()
        my_dict['__class__']: str = self.__class__.__name__
        my_dict['created_at']: str = str(self.created_at.isoformat())
        my_dict['updated_at']: str = str(self.updated_at.isoformat())
        return my_dict

# model = BaseModel()
# model.name: str = 'first name'
# model.my_number = 98
# # print(model)
# import time
# time.sleep(2)
# model.save()
# tojson = model.to_dict()
# print(tojson)
# # for key in tojson.keys():
# #     print(f'{key} {type(tojson[key])}')
# model = BaseModel(**tojson)
# print(model.to_dict())
