#!/usr/bin/python3
""" Module that contains class FileStorage """
from models import BaseModel
import json
import os.path


class FileStorage:
    """FileStorage class"""

    def __init__(self):
        self.__file_path: str = "file.json"
        self.__objects: dict = {}

    def reload(self) -> None:
        print("FileStorage.reload()>>>>>>>")

        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        else:
            print(f"File {self.__file_path} does not exist.")

    def save(self) -> None:
        print("FileStorage.save()>>>>>>>")
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def new(self, obj: BaseModel) -> None:
        print("FileStorage.new()>>>>>>>")
        self.__objects[obj.id] = obj.to_dict()
        pass

    def all(self) -> dict:
        print("FileStorage.all()>>>>>>>")
        return self.__objects
