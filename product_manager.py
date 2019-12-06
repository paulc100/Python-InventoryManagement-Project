from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from abstract_product import AbstractProduct
from product_stats import ProductStats
from computer import Computer
from cellphone import Cellphone
import json
import os.path

class ProductManager:
    """ This is the product manager """

    PRODUCT_LABEL = "Product Name"
    ID_LABEL = "ID"

    def __init__(self, db_name):
        """ Contructs a product object """
        if db_name is None or db_name == "":
            raise ValueError("DB Name cannot be undefined")

        engine = create_engine("sqlite:///" + db_name)
        self._db_session = sessionmaker(bind=engine, expire_on_commit=False)

    def add_product(self, product):
        """ Adds a product """

        AbstractProduct._validate_object_input("Product", product)

        id = product.get_id()

        if id is not None:
            product = self.get_product_by_id(id)
            if product is not None:
                raise ValueError("Product already exists!")

        session = self._db_session()

        session.add(product)
        session.commit()

        session.close()

        return product.get_id()

    def get_product_by_id(self, id):
        """ Returns a product with matching id, returns None if no matching id exists """
        AbstractProduct._validate_number_input(AbstractProduct.ID, id)
        session = self._db_session()
        
        product = session.query(Computer).filter(Computer.id == id).filter(Computer.type == AbstractProduct.COMPUTER_TYPE).first()
            
        if product is None:
            product = session.query(Cellphone).filter(Cellphone.id == id).filter(Cellphone.type == AbstractProduct.CELLPHONE_TYPE).first()

        session.close()
        return product

    def get_all(self):
        """ Retrieves all product objects """
        session = self._db_session()
        products1 = session.query(Computer).filter(Computer.type == AbstractProduct.COMPUTER_TYPE).all()
        products2 = session.query(Cellphone).filter(Cellphone.type == AbstractProduct.CELLPHONE_TYPE).all()
        products = products1 + products2

        session.close()
        return products

    def get_all_by_type(self, type):
        """ Retrieves all product objects from type """

        AbstractProduct._validate_string_input("Type", type)
        if type != AbstractProduct.CELLPHONE_TYPE and type != AbstractProduct.COMPUTER_TYPE:
            raise ValueError("Only computer or cellphone type is supported!")
        
        session = self._db_session()

        if type == AbstractProduct.COMPUTER_TYPE:
            products = session.query(Computer).filter(Computer.type == type).all()
        elif type == AbstractProduct.CELLPHONE_TYPE:
            products = session.query(Cellphone).filter(Cellphone.type == type).all()

        session.close()
        return products

    def update_product(self, product):
        """ Updates a product """

        AbstractProduct._validate_object_input("Product", product)
        product_id = product.get_id()

        if product_id == None:
            raise ValueError("Only existing products can be updated!")

        session = self._db_session()
        
        product_in_db = session.query(Computer).filter(Computer.id == product_id).first()
        if product_in_db is None:
            product_in_db = session.query(Cellphone).filter(Cellphone.id == product_id).first()
        
        if product_in_db is None:
            raise ValueError("Product does not exist in inventory!")

        if product_in_db.get_is_sold() == 1:
            raise ValueError("Product has already been sold!")

        product_in_db.set_price(product.get_price())

        if product.get_type() == AbstractProduct.COMPUTER_TYPE:
            product_in_db.set_case(product.get_case())
        elif product.get_type() == AbstractProduct.CELLPHONE_TYPE:
            product_in_db.set_camera(product.get_camera())

        session.commit()

        session.close()


    def remove_product_by_id(self, id):
        """ Removes a product via an id """

        AbstractProduct._validate_number_input(AbstractProduct.ID, id)
        session = self._db_session()

        product_in_db = session.query(AbstractProduct).filter(AbstractProduct.id == id).first()
        session.delete(product_in_db)
        session.commit()

        session.close()

    def get_product_stats(self):
        product_stats = ProductStats(self)
        return product_stats