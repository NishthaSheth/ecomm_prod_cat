from flask import Blueprint, request
from controllers.product_controller import ProductController

product = Blueprint('product',__name__)

@product.route('/create', methods = ['POST'])
def create_product():
    data = request.json
    return ProductController.create_product(data)

@product.route('<int:product_id>', methods = ['GET'])
def get_product(product_id):
    return ProductController.get_product_by_id(product_id)

@product.route('<int:product_id>', methods = ['PUT'])
def update_product(product_id):
    data = request.json
    return ProductController.update_product(product_id, data)

@product.route('<int:product_id>', methods = ['DELETE'])
def delete_product(product_id):
    return ProductController.delete_product(product_id)