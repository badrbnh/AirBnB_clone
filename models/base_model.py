#!/usr/bin/python3

from datetime import datetime
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs):
        tFormat = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
        else:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] == datetime.datetime.strptime(v, tFormat)
                else:
                    self.__dict__[k] == v

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict = {}
        dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            dict[key] = value
            if key == "created_at" or key == "updated_at":
                dict[key] = value.isoformat()

        return dict
