#!/usr/bin/python3
""" Module that contains class FileStorage """
from models import BaseModel


class FileStorage:
    """ FileStorage class """
    def __init__(self, path: str):
        self.__file_path: str = path
        self.__objects: dict = {}

    def reload(self) -> None:
        pass

    def save(self) -> None:
        pass

    def new(self, obj: BaseModel) -> None:
        pass

    def all(self) -> dict:
        return self.__objects
