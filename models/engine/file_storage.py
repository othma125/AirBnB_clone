#!/usr/bin/python3
""" Module that contains class FileStorage """
from json import load, dump
import os.path


class FileStorage:
    """FileStorage class"""
    __file_path: str = "file.json"
    __objects: dict = {}

    @property
    def file_path(self):
        return self.__file_path

    def all(self) -> dict:
        """return data dict"""
        return self.__objects

    def reload(self) -> None:
        """reload method"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                self.__objects = load(f)

    def save(self) -> None:
        """save"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            dump(self.__objects, f)

    def new(self, obj) -> None:
        """new element is added to dic"""
        key: str = obj.__class__.__name__ + "." + obj.id
        self.__objects.update({key: obj.to_dict()})
