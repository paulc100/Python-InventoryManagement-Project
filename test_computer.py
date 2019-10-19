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
        self.logPoint()
        self._computer = Computer(1, "Huawei Matebook X Pro", 1600, 1200, "7/21/19", "8/23/19", True, "Nvidia Geforce", "Dbrand", "DDR4")
        self.assertIsNotNone(self._computer)

    def tearDown(self):
        self._computer = None
        
    def logPoint(self):
        currentTest= self.id().split('.')[-1]
        callingFunction= inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_get_id(self):
        self.assertEqual(1, self._computer.get_id())

    def test_get_name(self):
        self.assertEqual("Huawei Matebook X Pro", self._computer.get_name())

    def test_get_price(self):
        self.assertEqual(1600, self._computer.get_price())

    def test_set_price(self):
        old_price = self._computer.get_price()
        new_price = old_price + 100
        self._computer.set_price(new_price)
        self.assertEqual(new_price, self._computer.get_price())

    def test_get_cost(self):
        self.assertEqual(1200, self._computer.get_cost())

    def test_get_date_stocked(self):
        self.assertEqual("7/21/19", self._computer.get_date_stocked())

    def test_get_date_sold(self):
        self.assertEqual("8/23/19", self._computer.get_date_sold())

    def test_get_is_sold(self):
        self.assertEqual(True, self._computer.get_is_sold())

    def test_get_details(self):

        expected_details = "Your " + self._computer.get_type() \
        + " is a " + self._computer.get_name() \
        + " that was stocked on " + self._computer.get_date_stocked() \
        + " and sold on " + self._computer.get_date_sold() \
        + " at the price of " + str(self._computer.get_price())
        self.assertEqual(expected_details, self._computer.get_details())

    def test_get_type(self):
        self.assertEqual("computer", self._computer.get_type())

    def test_get_graphics_card(self):
        self.assertEqual("Nvidia Geforce", self._computer.get_graphics_card())

    def test_get_case(self):
        self.assertEqual("Dbrand", self._computer.get_case())

    def test_get_memory_type(self):
        self.assertEqual("DDR4", self._computer.get_memory_type())

if __name__ == "__main__":
    unittest.main()
