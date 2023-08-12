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

        # Initialize __objects for testing
        self.instance.__objects = self.test_data

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all_method(self):
        result = self.instance.all()
        self.assertEqual(result, self.test_data)

    def test_new_method(self):
        new_model = BaseModel()
        self.instance.new(new_model)
        key = f"{new_model.__class__.__name__}.{new_model.id}"
        self.assertIn(key, self.instance._FileStorage__objects)

    def test_save_method(self):
        self.instance.__file_path = self.file_path
        self.instance.save()

        with open(self.file_path, "r") as data_file:
            saved_data = json.load(data_file)

        expected_data = {}
        for key, value in self.test_data.items():
            expected_data[key] = value.to_dict()

        self.assertEqual(saved_data, expected_data)

    def test_reload_method(self):
        # Save test data to file
        self.instance.__objects = self.test_data
        self.instance.__file_path = self.file_path
        self.instance.save()

        # Clear objects and reload from file
        self.instance.__objects = {}
        self.instance.reload()

        self.assertEqual(self.instance.all(), self.test_data)
