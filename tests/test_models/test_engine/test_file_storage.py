import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = storage._FileStorage__file_path
        self.instance = BaseModel()
        self._objs = storage._FileStorage__objects
        self.keyname = "BaseModel."+self.instance.id

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all_method(self):
        result = storage.all()
        self.assertEqual(result, self._objs)

    def test_new_method(self):
        storage.new(self.instance)
        key = f"{self.instance.__class__.__name__}.{self.instance.id}"
        self.assertIn(key, self._objs)

    def test_save_method(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        storage.save()
        with open(self.file_path, "r") as data_file:
            saved_data = json.load(data_file)

        expected_data = {}
        for key, value in self._objs.items():
            expected_data[key] = value.to_dict()

        self.assertEqual(saved_data, expected_data)

    def test_reload_method(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        storage.save()
        with open(self.file_path, 'r') as file:
            saved_data = json.load(file)
        storage.reload()

        with open(self.file_path, 'r') as file:
            reloaded_data = json.load(file)

        self._objs = {}
        self.assertEqual(reloaded_data[self.keyname], saved_data[self.keyname])


if __name__ == "__main__":
    unittest.main()
