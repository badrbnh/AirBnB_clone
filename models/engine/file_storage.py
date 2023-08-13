#!/usr/bin/python3

"""
FileStorage Module

This module manages the serialization and deserialization
of objects to and from JSON files.

Classes:
- FileStorage: Manages the storage and
retrieval of instances to/from JSON files.

Attributes:
- __file_path (str): The path to the JSON file.
- __objects (dict): A dictionary to store instances by their class name and ID.

Methods:
- all(self): Returns the dictionary of stored objects.
- new(self, obj): Adds an object to the storage.
- save(self): Serializes the objects and saves to the JSON file.
- reload(self): Deserializes the JSON file and loads objects.

Usage:
from models.engine.file_storage import FileStorage

# Instantiate FileStorage
storage = FileStorage()

# Load existing object data from the JSON file
storage.reload()

# Perform operations on instances (create, update, delete)
# Call storage.save() after each operation to persist changes

"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
import json
import os
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
