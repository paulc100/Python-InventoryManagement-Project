from abstract_product import AbstractProduct
from computer import Computer
from cellphone import Cellphone

class ProductManager:
    """ This is the product manager """

    _products = []
    _next_available_id = 1

    def __init__(self):
        """ Constructs a product object """
        return

    def add(self, product):
        """ Adds a product to the manager """

        if product in self._products:
            raise ValueError("Product already exists in the inventory")
        else:
            unique_id = self._next_available_id

            product.set_id(unique_id)
            self._products.append(product)
            self._next_available_id = unique_id + 1
            return unique_id

    def get(self, id):
        """ Retrieves product object from id """
        for product in self._products:
            if product.get_id() == id:
                return product
        return None

    def get_all(self):
        """ Retrieves all product objects """
        return self._products

    def get_all_by_type(self, type):
        """ Retrieves all product objects from type """
        products = []
        for product in self._products:
            if product.get_type() == type:
                products.append(product)
        return products

    def update(self, product):
        """ Replaces a product with a new one """
        for prod in self._products:
            if prod.get_id() == product.get_id():
                self._products.remove(prod)
                self._products.append(product)
                return
        raise ValueError("%d does not exist." %(product.get_id()))

    def delete(self, id):
        """ Removes a product via an id """
        for product in self._products:
            if product.get_id() == id:
                self._products.remove(product)
                return
        raise ValueError("%d does not exist." %(product.get_id()))