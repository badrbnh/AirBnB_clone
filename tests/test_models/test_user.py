import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

class TestUser(unittest.TestCase):

    def setUp(self):
        self.test_user = User()
        self.test_user.first_name = "John"
        self.test_user.last_name = "Doe"
        self.test_user.email = "john.doe@example.com"
        self.test_user.password = "secretpassword"

    def tearDown(self):
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        self.assertIsInstance(self.test_user, BaseModel)
        self.assertIsInstance(self.test_user, User)

    def test_attributes(self):
        self.assertEqual(self.test_user.first_name, "John")
        self.assertEqual(self.test_user.last_name, "Doe")
        self.assertEqual(self.test_user.email, "john.doe@example.com")
        self.assertEqual(self.test_user.password, "secretpassword")

    def test_to_dict_method(self):
        user_dict = self.test_user.to_dict()
        self.assertTrue("id" in user_dict)
        self.assertTrue("created_at" in user_dict)
        self.assertTrue("updated_at" in user_dict)
        self.assertTrue("first_name" in user_dict)
        self.assertTrue("last_name" in user_dict)
        self.assertTrue("email" in user_dict)
        self.assertTrue("password" in user_dict)
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")
        self.assertEqual(user_dict["email"], "john.doe@example.com")
        self.assertEqual(user_dict["password"], "secretpassword")

    def test_str_representation(self):
        expected_str = "[User] ({}) {}".format(
            self.test_user.id, self.test_user.__dict__)
        self.assertEqual(str(self.test_user), expected_str)

if __name__ == "__main__":
    unittest.main()
