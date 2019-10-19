class AbstractProduct:
    """This is the representation of a product"""
    
    def __init__(self, id, name, price, cost, date_stocked, date_sold, is_sold):
        """Makes abstract product object"""

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
        self._id = id

    def get_name(self):
        """Gets product name"""
        return self._name

    def get_price(self):
        """Gets product price"""
        return self._price

    def set_price(self, price):
        """Sets product price"""
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
