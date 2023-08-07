#!/usr/bin/python3
""" Module that contains class FileStorage """
from json import load, dump
import os.path


class FileStorage:
    """FileStorage class"""

    def __init__(self):
        """ constructor """
        self.__file_path: str = "file.json"
        self.__objects: dict = {}

    def reload(self) -> None:
        """ reload method """
        # print("FileStorage.reload()>>>>>>>")
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = load(f)
        # else:
        #     print(f"File {self.__file_path} does not exist.")

    def save(self) -> None:
        """ save """
        # print("FileStorage.save()>>>>>>>")
        with open(self.__file_path, "w") as f:
            dump(self.__objects, f)

    def new(self, obj) -> None:
        """ new element is added to dic """
        # print("FileStorage.new()>>>>>>>")
        key: str = obj.__class__.__name__ + "." + obj.id
        self.__objects.update({key: obj.to_dict()})

    def all(self) -> dict:
        """ return data dict """
        # print("FileStorage.all()>>>>>>>")
        return self.__objects
