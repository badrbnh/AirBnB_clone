#!/usr/bin/python3
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}
        
    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
        
    
    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        serialized_objects = {}
        for obj_key, obj_value in self.__objects.items():
            serialized_objects[obj_key] = obj_value.to_dict()
        with open(self.__file_path, "w") as data_file:
            json.dump(serialized_objects, data_file, indent=4)
            
    
    def reload(self):
        if self.__file_path is not None:
            try:
                with open(self.__file_path, "r") as data_file:
                    json_data = json.load(data_file)
                    for key, value in json_data.items():
                        self.__objects[key] = value
            except FileNotFoundError:
                pass