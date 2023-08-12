#!/usr/bin/python3
import json
from models.base_model import BaseModel
import os


class FileStorage:
    """
    This class manages the serialization and deserialization
    of objects to and from JSON files.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary containing all stored objects.
        Returns:
            dict: A dictionary containing all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj (BaseModel): The object to be added to the storage.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        data = {}

        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as file:          
            json.dump(data, file, indent=4)

    def reload(self):
        """
        Deserializes the JSON file to __objects (if the JSON file exists).
        """
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, "r", encoding="utf-8") as data_file:
                    json_data = json.load(data_file)
                    for key, value in json_data.items():
                        if '.' in key:
                            class_name, obj_id = key.split('.')
                            class_obj = globals()[class_name]
                            new_instance = class_obj(**value)
                            self.new(new_instance)
                            self.__objects[key] = new_instance
            except FileNotFoundError:
                pass
