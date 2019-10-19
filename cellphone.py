from abstract_product import AbstractProduct

class Cellphone(AbstractProduct):
    
    _CELLPHONE_TYPE = "Cellphone"
    
    """Representation of a Cellphone"""
    def __init__(self, id, name, price, cost, date_stocked, date_sold, is_sold, camera, security, screen_body_ratio):
        AbstractProduct._validate_string_input(AbstractProduct.CAMERA, camera)
        AbstractProduct._validate_string_input(AbstractProduct.SECURITY, security)
        AbstractProduct._validate_string_input(AbstractProduct.SCREEN_BODY_RATIO, screen_body_ratio)
        
        super().__init__(id, name, price, cost, date_stocked, date_sold, is_sold)
        self._camera = camera
        self._security = security
        self._screen_body_ratio = screen_body_ratio

    """Gets camera details"""
    def get_camera(self):
        return self._camera

    """Gets security details"""
    def get_security(self):
        return self._security

    """Gets screen to body ratio details"""
    def get_screen_body_ratio(self):
        return self._screen_body_ratio

    """Gets all details of cellphone"""
    def get_details(self):

        details = "Your " + self._CELLPHONE_TYPE \
        + " is a " + self._name \
        + " that was stocked on " + self._date_stocked \
        + " and sold on " + self._date_sold \
        + " at the price of " + str(self._price)
        return details

    """Gets the type"""
    def get_type(self):
        return self._CELLPHONE_TYPE