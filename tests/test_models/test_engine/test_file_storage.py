import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize FileStorage and BaseModel instances
        storage._FileStorage__objects = {}
        cls.file_path = storage._FileStorage__file_path
        cls.instance = BaseModel()
        cls.keyname = f"{cls.instance.__class__.__name__}.{cls.instance.id}"

    @classmethod
    def tearDownClass(cls):
        # Clean up by removing the test file
        try:
            os.remove(cls.file_path)
        except FileNotFoundError:
            pass

    def setUp(self):
        # Reset objects dictionary before each test
        storage._FileStorage__objects = {}

    def test_all_method(self):
        storage._FileStorage__objects[self.keyname] = self.instance
        result = storage.all()
        self.assertEqual(result, storage._FileStorage__objects)

    def test_new_method(self):
        storage.new(self.instance)
        self.assertIn(self.keyname, storage._FileStorage__objects)

    def test_save_method(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        storage.new(my_model)
        storage.save()

        with open(self.file_path, "r") as data_file:
            saved_data = json.load(data_file)

        self.assertEqual(saved_data[self.keyname], my_model.to_dict())

    def test_reload_method(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        storage.new(my_model)
        storage.save()

        with open(self.file_path, 'r') as file:
            saved_data = json.load(file)

        storage.reload()

        with open(self.file_path, 'r') as file:
            reloaded_data = json.load(file)

        self.assertEqual(reloaded_data[self.keyname], saved_data[self.keyname])


if __name__ == "__main__":
    unittest.main()
