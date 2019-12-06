from abstract_product import AbstractProduct
from sqlalchemy import *

class Computer(AbstractProduct):

    graphics_card = Column(String(100))
    case = Column(String(100))
    memory_type = Column(String(100))

    def __init__(self, name, price, cost, date_stocked, date_sold, is_sold, graphics_card, case, memory_type):
        """Representation of a computer"""
        AbstractProduct._validate_string_input(AbstractProduct.GRAPHICS_CARD, graphics_card)
        AbstractProduct._validate_string_input(AbstractProduct.CASE, case)
        AbstractProduct._validate_string_input(AbstractProduct.MEMORY_TYPE, memory_type)
        
        super().__init__(name, price, cost, date_stocked, date_sold, is_sold, AbstractProduct.COMPUTER_TYPE)
        self.graphics_card = graphics_card
        self.case = case
        self.memory_type = memory_type

    def get_graphics_card(self):
        """Gets graphics card details"""
        return self.graphics_card

    def get_case(self):
        """Gets case details"""
        return self.case

    def set_case(self, case):
        self.case = case

    def get_memory_type(self):
        """Gets memory type details"""
        return self.memory_type

    def get_details(self):
        """Gets all details of computer"""

        details = "Your " + AbstractProduct.COMPUTER_TYPE \
        + " is a " + self.name \
        + " that was stocked on " + self.date_stocked \
        + " and sold on " + self.date_sold \
        + " at the price of " + str(self.price)
        return details

    def to_dict(self):
        dict = {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "cost": self.cost,
            "date_stocked": self.date_stocked,
            "date_sold": self.date_sold,
            "is_sold": self.is_sold,
            "graphics_card": self.graphics_card,
            "case": self.case,
            "memory_type": self.memory_type,
            "type": AbstractProduct.COMPUTER_TYPE
        }
        return dict