class AbstractProduct:
    """This is the representation of a product """

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

    def __init__(self, id, name, price, cost, date_stocked, date_sold, is_sold):
        """This is the constructor of a product"""

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
    
    def get_id(self):
        """Gets product id"""
        return self._id

    def set_id(self, id):
        """Sets product id"""
        AbstractProduct._validate_number_input(AbstractProduct.ID, id)
        self._id = id

    def get_name(self):
        """Gets product name"""
        return self._name

    def get_price(self):
        """Gets product price"""
        return self._price

    def set_price(self, price):
        """Sets product price"""
        AbstractProduct._validate_number_input(AbstractProduct.PRICE, price)
        self._price = price

    def get_cost(self):
        """Gets product cost"""
        return self._cost

    def get_date_stocked(self):
        """Gets date that product is stocked"""
        return self._date_stocked

    def get_date_sold(self):
        """Gets date that product is sold"""
        return self._date_sold

    def get_is_sold(self):
        """Returns a boolean to see if product is sold or not"""
        return self._is_sold

    def get_details(self):
        """Gets product details"""
        raise NotImplementedError('Abstract method not implemented yet')

    def get_type(self):
        """Gets product type"""
        raise NotImplementedError('Abstract method not implemented yet')

    def to_dict(self):
        """Abstract Method for creating dictionaries"""
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