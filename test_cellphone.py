from unittest import TestCase
import unittest
from cellphone import Cellphone
from computer import Computer
from abstract_product import AbstractProduct
import re
import inspect

class TestCellphone(TestCase):
    """ Unit Tests for the Cellphone Class """

    _cellphone = None

    def setUp(self):
        self.logPoint()
        self._cellphone = Cellphone(2, "Pixel 4", 1000, 500, "10/15/19", "10/16/19", True, "G Camera", "Google Lock", 88)
        self.assertIsNotNone(self._cellphone)

    def tearDown(self):
        self._cellphone = None
        
    def logPoint(self):
        currentTest= self.id().split('.')[-1]
        callingFunction= inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_get_id(self):
        self.assertEqual(2, self._cellphone.get_id())

    def test_get_name(self):
        self.assertEqual("Pixel 4", self._cellphone.get_name())

    def test_get_price(self):
        self.assertEqual(1000, self._cellphone.get_price())

    def test_set_price(self):
        old_price = self._cellphone.get_price()
        new_price = old_price + 100
        self._cellphone.set_price(new_price)
        self.assertEqual(new_price, self._cellphone.get_price())

    def test_get_cost(self):
        self.assertEqual(500, self._cellphone.get_cost())

    def test_get_date_stocked(self):
        self.assertEqual("10/15/19", self._cellphone.get_date_stocked())

    def test_get_date_sold(self):
        self.assertEqual("10/16/19", self._cellphone.get_date_sold())

    def test_get_is_sold(self):
        self.assertEqual(True, self._cellphone.get_is_sold())

    def test_get_details(self):

        expected_details = "Your " + self._cellphone.get_type() \
        + " is a " + self._cellphone.get_name() \
        + " that was stocked on " + self._cellphone.get_date_stocked() \
        + " and sold on " + self._cellphone.get_date_sold() \
        + " at the price of " + str(self._cellphone.get_price())
        self.assertEqual(expected_details, self._cellphone.get_details())

    def test_get_type(self):
        self.assertEqual("cellphone", self._cellphone.get_type())

    def test_get_camera(self):
        self.assertEqual("G Camera", self._cellphone.get_camera())

    def test_get_security(self):
        self.assertEqual("Google Lock", self._cellphone.get_security())

    def test_get_screen_body_ratio(self):
        self.assertEqual(88, self._cellphone.get_screen_body_ratio())


if __name__ == "__main__":
    unittest.main()
