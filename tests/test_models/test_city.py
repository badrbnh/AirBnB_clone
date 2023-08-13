#!/usr/bin/python3

import unittest
from models.city import City


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.new_user = City()

    def tearDown(self):
        del self.new_user

    def test_user_type(self):
        self.assertEqual(self.new_user.state_id, "")
        self.assertEqual(self.new_user.name, "")

    def test_user_attribute(self):
        self.new_user.name = "Root"
        self.new_user.name = "h35df"

        self.assertEqual(self.new_user.name, "Root")
        self.assertEqual(self.new_user.state_id, "h35df")


if __name__ == '__main__':
    unittest.main()
