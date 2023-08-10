#!/usr/bin/python3
import json
from models.base_model import BaseModel


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
        try:
            with open(self.__file_path, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}

        serialized_objects = {}
        for obj_key, obj_value in self.__objects.items():
            serialized_objects[obj_key] = obj_value.to_dict()

        data.update(serialized_objects)

        with open(self.__file_path, "w") as data_file:
            json.dump(data, data_file, indent=4)

    def reload(self):
        """
        Deserializes the JSON file to __objects (if the JSON file exists).
        """
        if self.__file_path is not None:
            try:
                with open(self.__file_path, "r") as data_file:
                    json_data = json.load(data_file)
                    for key, value in json_data.items():
                        class_name, obj_id = key.split('.')
                        class_obj = globals()[class_name]
                        self.__objects[key] = class_obj(**value)
            except FileNotFoundError:
                pass
