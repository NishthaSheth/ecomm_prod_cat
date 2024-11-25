from flask import Blueprint, request
from controllers.category_controller import CategoryController

category = Blueprint('category',__name__)

@category.route('/create',methods = ['POST'])
def create_category():
    data = request.json
    return CategoryController.create_category(data)

@category.route('<int:category_id>', methods = ['GET'])
def get_category(category_id):
    return CategoryController.get_category(category_id)

@category.route('/',methods = ['GET'])
def get_all_categories():
    return CategoryController.get_all_categories()

@category.route('<int:category_id>', methods = ['PUT'])
def update_category(category_id):
    data = request.json
    return CategoryController.update_category(category_id, data)

@category.route('<int:category_id>', methods = ['DELETE'])
def delete_category(category_id):
    return CategoryController.delete_category(category_id)