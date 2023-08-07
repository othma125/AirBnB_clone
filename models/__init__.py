#!/usr/bin/python3
"""
    instantiates the storage system, and defines
    classes for further use
"""
import models
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

classes_dict = {'BaseModel': BaseModel, 'User': User}
storage: FileStorage = FileStorage()
storage.reload()
