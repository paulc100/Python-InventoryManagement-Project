from abstract_product import AbstractProduct
from product_stats import ProductStats
from computer import Computer
from cellphone import Cellphone
import json
import os.path

class ProductManager:
    """ This is the product manager """

    _products = []
    _next_available_id = 1
    _filepath = None

    def __init__(self, filepath):
        """ Constructs a product object """
        self._filepath = filepath
        self._read_products_from_file()

    def add_product(self, product):
        """ Adds a product to the manager """

        AbstractProduct._validate_object_input("Product", product)
        if product in self._products:
            raise ValueError("Product already exists in the inventory")
        else:
            unique_id = self._next_available_id

            product.set_id(unique_id)
            self._products.append(product)
            self._write_products_to_file()
            self._next_available_id = unique_id + 1
            return unique_id

    def get_product_by_id(self, id):
        """ Retrieves product object from id """

        AbstractProduct._validate_number_input(AbstractProduct.ID, id)
        for product in self._products:
            if product.get_id() == id:
                return product
        return None

    def get_all(self):
        """ Retrieves all product objects """

        return self._products

    def get_all_by_type(self, type):
        """ Retrieves all product objects from type """

        AbstractProduct._validate_string_input("Type", type)
        if type != AbstractProduct.CELLPHONE_TYPE and type != AbstractProduct.COMPUTER_TYPE:
            raise ValueError("Only computer or cellphone type is supported!")
        products = []
        for product in self._products:
            if product.get_type() == type:
                products.append(product)
        return products

    def update_product(self, product):
        """ Replaces a product with a new one """

        AbstractProduct._validate_object_input("Product", product)
        should_update = False
        for prod in self._products:
            if prod.get_id() == product.get_id():
                self._products.remove(prod)
                self._products.append(product)
                self._write_products_to_file()
                return
        raise ValueError("%d does not exist." %(product.get_id()))

    def remove_product_by_id(self, id):
        """ Removes a product via an id """

        AbstractProduct._validate_number_input(AbstractProduct.ID, id)
        for product in self._products:
            if product.get_id() == id:
                self._products.remove(product)
                self._write_products_to_file()
                return
        raise ValueError("%d does not exist." %(id))

    def get_product_stats(self):
        product_stats = ProductStats(self)
        return product_stats

    def _read_products_from_file(self):
        #print("_read_products_from_file() is called")
        if not os.path.exists(self._filepath):
            return

        with open(self._filepath, 'r') as input_file:
            data = json.load(input_file)
            largest_id = 0
            for json_data in data:
                type = json_data["type"]
                if type == AbstractProduct.COMPUTER_TYPE:
                    id = json_data["id"]
                    name = json_data["name"]
                    price = json_data["price"]
                    cost = json_data["cost"]
                    date_stocked = json_data["date_stocked"]
                    date_sold = json_data["date_sold"]
                    is_sold = json_data["is_sold"]
                    graphics_card = json_data["graphics_card"]
                    case = json_data["case"]
                    memory_type = json_data["memory_type"]
                    product = Computer(id, name, price, cost, date_stocked, date_sold, is_sold, graphics_card, case, memory_type)
                elif type == AbstractProduct.CELLPHONE_TYPE:
                    id = json_data["id"]
                    name = json_data["name"]
                    price = json_data["price"]
                    cost = json_data["cost"]
                    date_stocked = json_data["date_stocked"]
                    date_sold = json_data["date_sold"]
                    is_sold = json_data["is_sold"]
                    camera = json_data["camera"]
                    security = json_data["security"]
                    screen_body_ratio = json_data["screen_body_ratio"]
                    product = Cellphone(id, name, price, cost, date_stocked, date_sold, is_sold, camera, security, screen_body_ratio)
                self._products.append(product)
                if largest_id < id:
                    largest_id = id
            self._next_available_id = largest_id + 1

    def _write_products_to_file(self):
        #print("_write_products_to_file() is called")
        data = []
        for product in self._products:
            json_data = product.to_dict()
            data.append(json_data)
        #print(data)
        with open(self._filepath, 'w+') as output_file:
            json.dump(data, output_file)