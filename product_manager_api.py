from flask import Flask, request
from product_manager import ProductManager
from product_stats import ProductStats
from abstract_product import AbstractProduct
from cellphone import Cellphone
from computer import Computer
import json

app = Flask(__name__)
prod_manager = ProductManager("products.sqlite")

@app.route('/product_manager/products', methods=['POST'])
def add_product():
    """ Adds a product to products """
    content = request.json
    try:
        id = None
        type = None
        product = None
        if content["type"] == AbstractProduct.CELLPHONE_TYPE:
            cellphone = Cellphone(content['name'], content['price'], content['cost'], content["date_stocked"], content["date_sold"], content["is_sold"], content["camera"], content["security"], content["screen_body_ratio"])
            prod_manager.add_product(cellphone)
            id = cellphone.get_id()
            type = cellphone.get_type()
            product = cellphone
        elif content["type"] == AbstractProduct.COMPUTER_TYPE:
            computer = Computer(content["name"], content["price"], content["cost"], content["date_stocked"], content["date_sold"], content["is_sold"], content["graphics_card"], content["case"], content["memory_type"])
            prod_manager.add_product(computer)
            id = computer.get_id()
            type = computer.get_type()
            product = computer
        print("id = ", id)
        print("type = ", type)
        print("prod = ", product.to_dict())
        response = app.response_class(
            status=200
        )
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )
    return response

@app.route('/product_manager/products/<int:id>', methods=['PUT'])
def update_product(id):
    """ Updates a product by id """
    content = request.json
    product = prod_manager.get_product_by_id(id)

    if product == None:
        response = app.response_class(
            status=404
        )
        return response
        
    try:
        product.set_price(content["price"])
        type = product.get_type()

        if type == AbstractProduct.CELLPHONE_TYPE:
            product.set_camera(content["camera"])
        elif type == AbstractProduct.COMPUTER_TYPE:
            product.set_case(content["case"])

        prod_manager.update_product(product)
        
        response = app.response_class(
            status=200
        )
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400
        )
    return response

@app.route('/product_manager/products/<int:id>', methods=['DELETE'])
def remove_product_by_id(id):
    """ Removes a product by id """
    try:
        product = prod_manager.remove_product_by_id(id)
        response = app.response_class(
            status=200
        )
    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
    return response

@app.route('/product_manager/products/<int:id>', methods=['GET'])
def get_product_by_id(id):
    """ Gets product by id """
    try:
        product = prod_manager.get_product_by_id(id)
        if product != None:
            response = app.response_class(
                status=200,
                response=json.dumps(product.to_dict()),
                mimetype='application/json'
            )
            return response
    
    except ValueError:
        pass

    else:
        response = app.response_class(
        status=404
        )
    return response

@app.route('/product_manager/products/all', methods=['GET'])
def get_all():
    """ Gets all products """
    products = prod_manager.get_all()
    data = []
    for product in products:
        json_data = product.to_dict()
        data.append(json_data)

    response = app.response_class(
            status=200,
            response=json.dumps(data),
            mimetype='application/json'
        )
    return response

@app.route('/product_manager/products/all/<string:type>', methods=['GET'])
def get_all_by_type(type):
    """ Gets all by type """
    try:
        print('type: ', type)
        products = prod_manager.get_all_by_type(type)
        data = []
        for product in products:
            json_data = product.to_dict()
            data.append(json_data)

        response = app.response_class(
                status=200,
                response=json.dumps(data),
                mimetype='application/json'
            )
    except ValueError as e:
        response = app.response_class(response=str(e), status=400)

    return response

@app.route('/product_manager/products/stats', methods=['GET'])
def get_product_stats():
    """ Gets product stats """
    product_stats = prod_manager.get_product_stats()
    num_products = product_stats.get_total_num_products()
    num_computers = product_stats.get_num_computers()
    num_cellphones = product_stats.get_num_cellphones()
    avg_computer_profit = product_stats.get_avg_computer_profit()
    avg_cellphone_profit = product_stats.get_avg_cellphone_profit()
    avg_computer_shelf_time = product_stats.get_avg_computer_shelf_time()
    avg_cellphone_shelf_time = product_stats.get_avg_cellphone_shelf_time()

    data = {}
    data["num_products"] = num_products
    data["num_computers"] = num_computers
    data["num_cellphones"] = num_cellphones
    data["avg_computer_profit"] = avg_computer_profit
    data["avg_cellphone_profit"] = avg_cellphone_profit
    data["avg_computer_shelf_time"] = avg_computer_shelf_time
    data["avg_cellphone_shelf_time"] = avg_cellphone_shelf_time

    response = app.response_class(
        status=200,
        response=json.dumps(data),
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run()