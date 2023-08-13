#!/usr/bin/python3
"""Unittest for the BaseModel Class """
import datetime
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """
    This class contains unittests for the BaseModel class.
    """
    def setUp(self):
        """Method that the setUp the cases to test"""
        self.my_model = BaseModel()
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89
        self.id = self.my_model.id
        self.type_1 = datetime.datetime
        self.my_model_json = self.my_model.to_dict()

    def tearDown(self):
        """Method to clean the tests"""
        del self.my_model

    def test_init_(self):
        """Test for The __init__ method in the BaseModel"""
        self.assertIsInstance(self.my_model, BaseModel)

    def test_new_attribue(self):
        """Test for the saving attributes"""
        self.assertEqual(self.my_model.name, "My_First_Model")
        self.assertEqual(self.my_model.my_number, 89)

    def test_id(self):
        """Test for the id generating"""
        self.assertEqual(self.id, self.my_model.id)

    def test_created_at(self):
        """Test for the type of created_at"""
        self.assertEqual(self.type_1, type(self.my_model.created_at))

    def test_to_dict(self):
        """Test for to_dic method"""
        self.assertEqual(self.my_model_json, self.my_model.to_dict())


if __name__ == '__main__':
    unittest.main()
