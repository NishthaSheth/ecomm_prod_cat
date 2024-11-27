from flask import Blueprint, request
from controllers.product_controller import ProductController
from library.functions import jwt_required

product = Blueprint('product',__name__)

@product.route('/insert', methods = ['POST'])
@jwt_required
def create_product():
    data = request.json
    return ProductController.create_product(data)

@product.route('/<int:product_id>', methods = ['GET'], endpoint = 'get_product')
@jwt_required
def get_product(product_id):
    return ProductController.get_product_by_id(product_id)

@product.route('/<int:product_id>', methods = ['PUT'], endpoint = 'update_product')
@jwt_required
def update_product(product_id):
    data = request.json
    return ProductController.update_product(product_id, data)

@product.route('/<int:product_id>', methods = ['DELETE'], endpoint = 'del_product')
@jwt_required
def delete_product(product_id):
    return ProductController.delete_product(product_id)