from abstract_product import AbstractProduct

class Cellphone(AbstractProduct):
    
    _CELLPHONE_TYPE = "Cellphone"
    
    def __init__(self, id, name, price, cost, date_stocked, date_sold, is_sold, camera, security, screen_body_ratio):
        """Representation of a Cellphone"""
        AbstractProduct._validate_string_input(AbstractProduct.CAMERA, camera)
        AbstractProduct._validate_string_input(AbstractProduct.SECURITY, security)
        AbstractProduct._validate_string_input(AbstractProduct.SCREEN_BODY_RATIO, screen_body_ratio)
        
        super().__init__(id, name, price, cost, date_stocked, date_sold, is_sold)
        self._camera = camera
        self._security = security
        self._screen_body_ratio = screen_body_ratio

    def get_camera(self):
        """Gets camera details"""
        return self._camera

    def get_security(self):
        """Gets security details"""
        return self._security

    def get_screen_body_ratio(self):
        """Gets screen to body ratio details"""
        return self._screen_body_ratio

    def get_details(self):
        """Gets all details of cellphone"""

        details = "Your " + self._CELLPHONE_TYPE \
        + " is a " + self._name \
        + " that was stocked on " + self._date_stocked \
        + " and sold on " + self._date_sold \
        + " at the price of " + str(self._price)
        return details

    def get_type(self):
        """Gets the type"""
        return self._CELLPHONE_TYPE