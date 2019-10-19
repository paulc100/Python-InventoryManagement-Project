class AbstractProduct:

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

    """This is the representation of a product"""
    def __init__(self, id, name, price, cost, date_stocked, date_sold, is_sold):

        AbstractProduct._validate_number_input(AbstractProduct.ID, id)
        AbstractProduct._validate_string_input(AbstractProduct.NAME, name)
        AbstractProduct._validate_number_input(AbstractProduct.PRICE, price)
        AbstractProduct._validate_number_input(AbstractProduct.COST, cost)
        AbstractProduct._validate_string_input(AbstractProduct.DATE_STOCKED, date_stocked)
        AbstractProduct._validate_string_input(AbstractProduct.DATE_SOLD, date_sold)

        """Makes product object"""
        self._id = id
        self._name = name
        self._price = price
        self._cost = cost
        self._date_stocked = date_stocked
        self._date_sold = date_sold
        self._is_sold = is_sold
    
    """Gets product id"""
    def get_id(self):
        return self._id

    """Sets product id"""
    def set_id(self, id):
        AbstractProduct._validate_number_input(AbstractProduct.ID, id)
        self._id = id

    """Gets product name"""
    def get_name(self):
        return self._name

    """Gets product price"""
    def get_price(self):
        return self._price

    """Sets product price"""
    def set_price(self, price):
        AbstractProduct._validate_number_input(AbstractProduct.PRICE, price)
        self._price = price

    """Gets product cost"""
    def get_cost(self):
        return self._cost

    """Gets date that product is stocked"""
    def get_date_stocked(self):
        return self._date_stocked

    """Gets date that product is sold"""
    def get_date_sold(self):
        return self._date_sold

    """Returns a boolean to see if product is sold or not"""
    def get_is_sold(self):
        return self._is_sold

    """Gets product details"""
    def get_details(self):
        raise NotImplementedError('Abstract method not implemented yet')

    """Gets product type"""
    def get_type(self):
        raise NotImplementedError('Abstract method not implemented yet')

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