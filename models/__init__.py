#!/usr/bin/python3
"""
    instantiates the storage system, and defines
    classes for further use
"""
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

classes_dict = {'BaseModel': BaseModel}
storage: FileStorage = FileStorage()
storage.reload()
