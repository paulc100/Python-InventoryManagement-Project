from abstract_product import AbstractProduct

class Computer(AbstractProduct):
    """Representation of a computer"""

    _COMPUTER_TYPE = "computer"

    def __init__(self, id, name, price, cost, date_stocked, date_sold, is_sold, graphics_card, case, memory_type):
        """Constructs a Product with computer attributes"""
        
        super().__init__(id, name, price, cost, date_stocked, date_sold, is_sold)
        self._graphics_card = graphics_card
        self._case = case
        self._memory_type = memory_type
    
    def get_graphics_card(self):
        """Gets graphics card details"""
        return self._graphics_card

    def get_case(self):
        """Gets case model"""
        return self._case

    def get_memory_type(self):
        """Gets memory type details"""
        return self._memory_type

    def get_details(self):
        """Gets all details of computer"""

        details = "Your " + self._COMPUTER_TYPE \
        + " is a " + self._name \
        + " that was stocked on " + self._date_stocked \
        + " and sold on " + self._date_sold \
        + " at the price of " + str(self._price)
        return details

    def get_type(self):
        """Gets type of computer"""
        return self._COMPUTER_TYPE