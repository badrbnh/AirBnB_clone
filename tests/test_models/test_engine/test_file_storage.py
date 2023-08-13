import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """
    This class contains unittests for the FileStorage class.
    """

    def setUp(self):
        """
        Set up the test environment by creating instances and a FileStorage instance.
        """
        self.base_model1 = BaseModel()
        self.base_model2 = BaseModel()
        self.storage = FileStorage()

    def tearDown(self):
        """
        Clean up after each test by removing the test JSON file if it exists.
        """
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_instance_creation(self):
        """
        Test if an instance of FileStorage is created correctly.
        """
        self.assertIsInstance(self.storage, FileStorage)
        self.assertTrue(hasattr(self.storage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(self.storage, "_FileStorage__objects"))
    
    def test_all(self):
        """
        Test the all method of FileStorage.
        """
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, self.storage._FileStorage__objects)
    
    def test_new(self):
        """
        Test the new method of FileStorage.
        """
        new_obj = BaseModel()
        self.storage.new(new_obj)
        key = "{}.{}".format(type(new_obj).__name__, new_obj.id)
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_save_reload(self):
        """
        Test the save and reload methods of FileStorage.
        """
        self.storage.new(self.base_model1)
        self.storage.new(self.base_model2)
        self.storage.save()

        # Create a new FileStorage instance to simulate reloading
        new_storage = FileStorage()
        new_storage.reload()
        key1 = "{}.{}".format(type(self.base_model1).__name__, self.base_model1.id)
        key2 = "{}.{}".format(type(self.base_model2).__name__, self.base_model2.id)
        self.assertIn(key1, new_storage._FileStorage__objects)
        self.assertIn(key2, new_storage._FileStorage__objects)

if __name__ == "__main__":
    unittest.main()
