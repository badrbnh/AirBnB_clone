import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.test_data = {
            "key1": BaseModel(),
            "key2": BaseModel()
        }
        self.new_model = BaseModel()
        self.file_path = storage._FileStorage__file_path
        self.instance = FileStorage()
        self.instance.__objects = storage._FileStorage__objects
        self.key = f"{self.new_model.__class__.__name__}.{self.new_model.id}"

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all_method(self):
        result = self.instance.all()
        self.assertEqual(result, self.instance.all())

    def test_new_method(self):
        new_model = BaseModel()
        self.instance.new(new_model)
        key = f"{new_model.__class__.__name__}.{new_model.id}"
        self.assertIn(key, self.instance._FileStorage__objects)

    def test_save_method(self):
        self.instance.save()
        with open(self.file_path, 'r') as file:
            saved_data = json.load(file)

        self.assertIn(self.key, saved_data)
        self.assertEqual(saved_data[self.key], self.new_model.to_dict())

    def test_reload_method(self):
        self.instance.save()
        self.instance.reload()

        with open(self.file_path, 'r') as file:
            reloaded_data = json.load(file)

        self.assertIn(self.key, reloaded_data)
        self.assertEqual(reloaded_data[self.key], self.new_model.to_dict())


if __name__ == "__main__":
    unittest.main()
