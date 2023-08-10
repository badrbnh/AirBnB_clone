#!/usr/bin/python3
from models.base_model import BaseModel
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        v = FileStorage.__objects
        obj_dict = {k: v[k].to_dict() for k in v.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                objdict = json.load(f)
                for k, v in objdict.items():
                    cls_name = v['__class__']
                    cls_ex = globals().get(cls_name)
                    if cls_ex:
                        self.new(cls_ex(**v))
        except FileNotFoundError:
            return
