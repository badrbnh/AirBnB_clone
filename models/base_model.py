#!/usr/bin/python3

from datetime import datetime
import uuid
class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        dict = {}
        dict['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            dict[key] = value
            if key == 'created_at' or key == 'updated_at':
                dict[key] = value.isoformat()

        return dict
