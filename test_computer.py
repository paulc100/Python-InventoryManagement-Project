from unittest import TestCase
import unittest
from cellphone import Cellphone
from computer import Computer
from abstract_product import AbstractProduct
import re
import inspect

class TestComputer(TestCase):
    """ Unit Tests for the Computer Class """

    _computer = None

    def setUp(self):
        """ Create test computers """
        self.logPoint()
        self._computer = Computer(1, "Huawei Matebook X Pro", 1600, 1200, "7/21/19", "8/23/19", True, "Nvidia Geforce", "Dbrand", "DDR4")
        self.assertIsNotNone(self._computer)
    
    def logPoint(self):
        currentTest= self.id().split('.')[-1]
        callingFunction= inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def tearDown(self):
        """ Remove test computer """
        self._computer = None

    def test_get_id(self):
        """ 000A - Valid get_id """
        self.assertEqual(1, self._computer.get_id())

    def test_get_name(self):
        """ 020A - Valid get_name """
        self.assertEqual("Huawei Matebook X Pro", self._computer.get_name())

    def test_get_price(self):
        """ 030A - Valid get_price """
        self.assertEqual(1600, self._computer.get_price())

    def test_set_price(self):
        """ 040A - Valid set_price """
        old_price = self._computer.get_price()
        new_price = old_price + 100
        self._computer.set_price(new_price)
        self.assertEqual(new_price, self._computer.get_price())

    def test_set_price_invalid(self):
        """ 040B - Invalid set_price """
        undefined_price = None
        self.assertRaisesRegex(ValueError, "Price cannot be undefined.", self._computer.set_price, undefined_price)

        not_number_price = "not_number"
        self.assertRaisesRegex(ValueError, "Price is not a number!", self._computer.set_price, not_number_price)

    def test_get_cost(self):
        """ 050A - Valid get_cost """
        self.assertEqual(1200, self._computer.get_cost())

    def test_get_date_stocked(self):
        """ 060A - Valid get_date_stocked """
        self.assertEqual("7/21/19", self._computer.get_date_stocked())

    def test_get_date_sold(self):
        """ 070A - Valid get_date_sold """
        self.assertEqual("8/23/19", self._computer.get_date_sold())

    def test_get_is_sold(self):
        """ 080A - Valid get_is_sold """
        self.assertEqual(True, self._computer.get_is_sold())

    def test_get_details(self):
        """ 090A - Valid get_details """

        expected_details = "Your " + self._computer.get_type() \
        + " is a " + self._computer.get_name() \
        + " that was stocked on " + self._computer.get_date_stocked() \
        + " and sold on " + self._computer.get_date_sold() \
        + " at the price of " + str(self._computer.get_price())
        self.assertEqual(expected_details, self._computer.get_details())

    def test_get_type(self):
        """ 100A - Valid get_type """
        self.assertEqual(AbstractProduct.COMPUTER_TYPE, self._computer.get_type())

    def test_get_graphics_card(self):
        """ 110A - Valid get_graphics_card """
        self.assertEqual("Nvidia Geforce", self._computer.get_graphics_card())

    def test_get_case(self):
        """ 120A - Valid get_case """
        self.assertEqual("Dbrand", self._computer.get_case())

    def test_get_memory_type(self):
        """ 130A - Valid get_memory_type """
        self.assertEqual("DDR4", self._computer.get_memory_type())

    def test_to_dict(self):
        """ 140A - Valid get_details """
        expected_dict = {
            "id": self._computer.get_id(),
            "name": self._computer.get_name(),
            "price": self._computer.get_price(),
            "cost": self._computer.get_cost(),
            "date_stocked": self._computer.get_date_stocked(),
            "date_sold": self._computer.get_date_sold(),
            "is_sold": self._computer.get_is_sold(),
            "graphics_card": self._computer.get_graphics_card(),
            "case": self._computer.get_case(),
            "memory_type": self._computer.get_memory_type(),
            "type": self._computer.get_type()
        }
        self.assertEqual(expected_dict, self._computer.to_dict())

if __name__ == "__main__":
    unittest.main()
