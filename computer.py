from abstract_product import AbstractProduct

class Computer(AbstractProduct):

    _COMPUTER_TYPE = "Computer"

    """Representation of a computer"""
    def __init__(self, id, name, price, cost, date_stocked, date_sold, is_sold, graphics_card, case, memory_type):
        AbstractProduct._validate_string_input(AbstractProduct.GRAPHICS_CARD, graphics_card)
        AbstractProduct._validate_string_input(AbstractProduct.CASE, case)
        AbstractProduct._validate_string_input(AbstractProduct.MEMORY_TYPE, memory_type)
        
        super().__init__(id, name, price, cost, date_stocked, date_sold, is_sold)
        self._graphics_card = graphics_card
        self._case = case
        self._memory_type = memory_type
    
    """Gets graphics card details"""
    def get_graphics_card(self):
        return self._graphics_card

    """Gets case details"""
    def get_case(self):
        return self._case

    """Gets memory type details"""
    def get_memory_type(self):
        return self._memory_type

    """Gets all details of computer"""
    def get_details(self):

        details = "Your " + self._COMPUTER_TYPE \
        + " is a " + self._name \
        + " that was stocked on " + self._date_stocked \
        + " and sold on " + self._date_sold \
        + " at the price of " + str(self._price)
        return details

    """Gets type"""
    def get_type(self):
        return self._COMPUTER_TYPE