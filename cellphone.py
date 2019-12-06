from abstract_product import AbstractProduct
from sqlalchemy import *

class Cellphone(AbstractProduct):

    camera = Column(String(100))
    security = Column(String(100))
    screen_body_ratio = Column(String(100))
    
    def __init__(self, name, price, cost, date_stocked, date_sold, is_sold, camera, security, screen_body_ratio):
        """Representation of a Cellphone"""
        AbstractProduct._validate_string_input(AbstractProduct.CAMERA, camera)
        AbstractProduct._validate_string_input(AbstractProduct.SECURITY, security)
        AbstractProduct._validate_string_input(AbstractProduct.SCREEN_BODY_RATIO, screen_body_ratio)
        
        super().__init__(name, price, cost, date_stocked, date_sold, is_sold, AbstractProduct.CELLPHONE_TYPE)
        self.camera = camera
        self.security = security
        self.screen_body_ratio = screen_body_ratio

    def get_camera(self):
        """Gets camera details"""
        return self.camera

    def set_camera(self, camera):
        self.camera = camera

    def get_security(self):
        """Gets security details"""
        return self.security

    def get_screen_body_ratio(self):
        """Gets screen to body ratio details"""
        return self.screen_body_ratio

    def get_details(self):
        """Gets all details of cellphone"""

        details = "Your " + AbstractProduct.CELLPHONE_TYPE \
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
            "camera": self.camera,
            "security": self.security,
            "screen_body_ratio": self.screen_body_ratio,
            "type": AbstractProduct.CELLPHONE_TYPE
        }
        return dict