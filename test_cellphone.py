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
        """ Create test cellphones """
        self.logPoint()
        self._cellphone = Cellphone(2, "Pixel 4", 1000, 500, "10/15/19", "10/16/19", True, "G Camera", "Google Lock", 88)
        self.assertIsNotNone(self._cellphone)
    
    def logPoint(self):
        currentTest= self.id().split('.')[-1]
        callingFunction= inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def tearDown(self):
        """ Remove test cellphone """
        self._cellphone = None

    def test_get_id(self):
        """ 000A - Valid get_id """
        self.assertEqual(2, self._cellphone.get_id())

    def test_get_name(self):
        """ 020A - Valid get_name """
        self.assertEqual("Pixel 4", self._cellphone.get_name())

    def test_get_price(self):
        """ 030A - Valid get_price """
        self.assertEqual(1000, self._cellphone.get_price())

    def test_set_price(self):
        """ 040A - Valid set_price """
        old_price = self._cellphone.get_price()
        new_price = old_price + 100
        self._cellphone.set_price(new_price)
        self.assertEqual(new_price, self._cellphone.get_price())

    def test_set_price_invalid(self):
        """ 040B - Invalid set_price """
        undefined_price = None
        self.assertRaisesRegex(ValueError, "Price cannot be undefined.", self._cellphone.set_price, undefined_price)

        not_number_price = "not_number"
        self.assertRaisesRegex(ValueError, "Price is not a number!", self._cellphone.set_price, not_number_price)

    def test_get_cost(self):
        """ 050A - Valid get_cost """
        self.assertEqual(500, self._cellphone.get_cost())

    def test_get_date_stocked(self):
        """ 060A - Valid get_date_stocked """
        self.assertEqual("10/15/19", self._cellphone.get_date_stocked())

    def test_get_date_sold(self):
        """ 070A - Valid get_date_sold """
        self.assertEqual("10/16/19", self._cellphone.get_date_sold())

    def test_get_is_sold(self):
        """ 080A - Valid get_is_sold """
        self.assertEqual(True, self._cellphone.get_is_sold())

    def test_get_details(self):
        """ 090A - Valid get_details """

        expected_details = "Your " + self._cellphone.get_type() \
        + " is a " + self._cellphone.get_name() \
        + " that was stocked on " + self._cellphone.get_date_stocked() \
        + " and sold on " + self._cellphone.get_date_sold() \
        + " at the price of " + str(self._cellphone.get_price())
        self.assertEqual(expected_details, self._cellphone.get_details())

    def test_get_type(self):
        """ 100A - Valid get_type """
        self.assertEqual(AbstractProduct.CELLPHONE_TYPE, self._cellphone.get_type())

    def test_get_camera(self):
        """ 110A - Valid get_camera """
        self.assertEqual("G Camera", self._cellphone.get_camera())

    def test_get_security(self):
        """ 120A - Valid get_security """
        self.assertEqual("Google Lock", self._cellphone.get_security())

    def test_get_screen_body_ratio(self):
        """ 130A - Valid get_screen_body_ratio """
        self.assertEqual(88, self._cellphone.get_screen_body_ratio())

    def test_to_dict(self):
        """ 140A - Valid get_details """
        expected_dict = {
            "id": self._cellphone.get_id(),
            "name": self._cellphone.get_name(),
            "price": self._cellphone.get_price(),
            "cost": self._cellphone.get_cost(),
            "date_stocked": self._cellphone.get_date_stocked(),
            "date_sold": self._cellphone.get_date_sold(),
            "is_sold": self._cellphone.get_is_sold(),
            "camera": self._cellphone.get_camera(),
            "security": self._cellphone.get_security(),
            "screen_body_ratio": self._cellphone.get_screen_body_ratio(),
            "type": self._cellphone.get_type()
        }
        self.assertEqual(expected_dict, self._cellphone.to_dict())

if __name__ == "__main__":
    unittest.main()
