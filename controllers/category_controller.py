from flask import jsonify
from models.dbcategories import CategoryModel

class CategoryController:
    def create_category(data):
        name, description = data.get('name'), data.get('description')
        if not name:
            return jsonify({'status_code':0, 'status_message':'Missing name field'}),400
        
        category = CategoryModel.create_category(name, description)
        return jsonify({'status_code':1, 'status_message':'Category created successfully','data':category})
    
    def get_category(category_id):
        category = CategoryModel.get_category_by_id(category_id)
        if not category:
            return jsonify({'status_code':0,'status_message':'Category not found'}),404
        
        return jsonify({'status_code':1, 'status_message':'Category retrieved successfully','data':category})
    
    def get_all_categories():
        categories = CategoryModel.get_all_categories()
        return jsonify({'status_code':1, 'status_message':'Categories retrieved successfully','data':categories})
    
    def update_category(category_id, data):
        if not data:
            return jsonify({'status_code':0,'status_message':'No data found for updation'}),400
        
        res = CategoryModel.update_category(category_id, **data)
        if res:
            return jsonify({'status_code':1, 'status_message':'Category updated successfully'}),200
        return jsonify({'status_code':0,'status_message':'Category not found'}),404
    
    def delete_category(category_id):
        res = CategoryModel.delete_category(category_id)
        if res:
            return jsonify({'status_code':1,'status_message':'Category deleted successfully'}),200
        return jsonify({'status_code':0,'status_message':'Category not found'}),404
        