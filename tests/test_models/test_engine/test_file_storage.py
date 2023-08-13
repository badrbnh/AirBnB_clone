import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.test_data = {
            "key1": BaseModel(),
            "key2": BaseModel()
        }
        self.file_path = "test_file.json"
        self.instance = FileStorage()
        self.instance._FileStorage__objects = self.test_data  # Corrected the attribute name

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all_method(self):
        result = self.instance.all()
        self.assertEqual(result, self.instance._FileStorage__objects)

    def test_new_method(self):
        new_model = BaseModel()
        self.instance.new(new_model)
        key = f"{new_model.__class__.__name__}.{new_model.id}"
        self.assertIn(key, self.instance._FileStorage__objects)

      
        self.instance.save()
        with open(self.file_path, 'r') as file:
            saved_data = json.load(file)
        
        self.assertIn(key, saved_data)
        self.assertEqual(saved_data[key], new_model.to_dict())

        self.instance._FileStorage__objects.clear()
        self.instance.reload()

        with open(self.file_path, 'r') as file:
            reloaded_data = json.load(file)

        self.assertIn(key, reloaded_data)
        self.assertEqual(reloaded_data[key], new_model.to_dict())

        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.assertFalse(os.path.exists(self.file_path))
        self.instance.reload()

if __name__ == "__main__":
    unittest.main()
