from flask import Blueprint, request
from controllers.category_controller import CategoryController
from library.functions import jwt_required
category = Blueprint('category',__name__)

@category.route('/',methods = ['GET'], endpoint = 'get_all_categories')
@jwt_required
def get_all_categories():
    return CategoryController.get_all_categories()
@category.route('/create',methods = ['POST'], endpoint = 'create_category')
@jwt_required
def create_category():
    data = request.json
    return CategoryController.create_category(data)

@category.route('/<int:category_id>', methods = ['GET'], endpoint = 'get_category')
@jwt_required
def get_category(category_id):
    return CategoryController.get_category(category_id)

@category.route('/<int:category_id>', methods = ['PUT'], endpoint = 'update_category')
@jwt_required
def update_category(category_id):
    data = request.json
    return CategoryController.update_category(category_id, data)

@category.route('/<int:category_id>', methods = ['DELETE'], endpoint = 'delete_category')
@jwt_required
def delete_category(category_id):
    return CategoryController.delete_category(category_id)