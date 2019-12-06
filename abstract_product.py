from base import Base
from sqlalchemy import *

class AbstractProduct(Base):

    CELLPHONE_TYPE = "Cellphone"
    COMPUTER_TYPE = "Computer"

    ID = "ID"
    NAME = "Name"
    PRICE = "Price"
    COST = "Cost"
    DATE_STOCKED = "Date_stocked"
    DATE_SOLD = "Date_sold"

    GRAPHICS_CARD = "Graphics_card"
    CASE = "Case"
    MEMORY_TYPE = "Memory_type"

    CAMERA = "Camera"
    SECURITY = "Security"
    SCREEN_BODY_RATIO = "Screen body ratio"

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Integer)
    cost = Column(Integer)
    date_stocked = Column(String(100))
    date_sold = Column(String(100))
    is_sold = Column(Integer)
    type = Column(String(100))

    """This is the representation of a product"""
    def __init__(self, name, price, cost, date_stocked, date_sold, is_sold, type):

        AbstractProduct._validate_string_input(AbstractProduct.NAME, name)
        AbstractProduct._validate_number_input(AbstractProduct.PRICE, price)
        AbstractProduct._validate_number_input(AbstractProduct.COST, cost)
        AbstractProduct._validate_string_input(AbstractProduct.DATE_STOCKED, date_stocked)
        #AbstractProduct._validate_string_input(AbstractProduct.DATE_SOLD, date_sold)

        """Makes product object"""
        self.name = name
        self.price = price
        self.cost = cost
        self.date_stocked = date_stocked
        self.date_sold = date_sold
        self.is_sold = is_sold
        self.type = type

    """ Gets id """
    def get_id(self):
        return self.id

    """Gets product name"""
    def get_name(self):
        return self.name

    """Gets product price"""
    def get_price(self):
        return self.price

    """Sets product price"""
    def set_price(self, price):
        AbstractProduct._validate_number_input(AbstractProduct.PRICE, price)
        self.price = price

    """Gets product cost"""
    def get_cost(self):
        return self.cost

    """Gets date that product is stocked"""
    def get_date_stocked(self):
        return self.date_stocked

    """Gets date that product is sold"""
    def get_date_sold(self):
        return self.date_sold

    """Returns a boolean to see if product is sold or not"""
    def get_is_sold(self):
        return self.is_sold

    """Gets product details"""
    def get_details(self):
        raise NotImplementedError('Abstract method not implemented yet')

    """Gets product type"""
    def get_type(self):
        return self.type

    def to_dict(self):
        raise NotImplementedError("Abstract method not implemented yet")

    @staticmethod
    def _validate_string_input(display_name, str_value):
        """Private helper to validate string values"""
        if str_value is None:
            raise ValueError(display_name + " cannot be undefined.")
        if str_value == "":
            raise ValueError(display_name + " cannot be empty.")
    
    @staticmethod
    def _validate_number_input(display_name, num_value):
        """Private helper to validate number values"""
        if num_value is None:
            raise ValueError(display_name + " cannot be undefined.")
        if type(num_value) != int and type(num_value) != float:
            raise ValueError(display_name + " is not a number!")

    @staticmethod
    def _validate_object_input(display_name, obj_value):
        """Private helper to validate object values"""
        if obj_value is None:
            raise ValueError(display_name + " cannot be none.")