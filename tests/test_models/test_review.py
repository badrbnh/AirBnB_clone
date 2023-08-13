#!/usr/bin/python3

import unittest
from models.review import Review


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.new_user = Review()

    def tearDown(self):
        del self.new_user

    def test_user_type(self):
        self.assertEqual(self.new_user.place_id, "")
        self.assertEqual(self.new_user.user_id, "")
        self.assertEqual(self.new_user.text, "")

    def test_user_attribute(self):
        self.new_user.place_id = "f45edf6"
        self.new_user.user_id = "435fze"
        self.new_user.text = "Hello world"

        self.assertEqual(self.new_user.place_id, "f45edf6")
        self.assertEqual(self.new_user.user_id, "435fze")
        self.assertEqual(self.new_user.text, "Hello world")


if __name__ == '__main__':
    unittest.main()
