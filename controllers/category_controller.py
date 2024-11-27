from models.dbcategories import CategoryModel
from library.functions import functions

class CategoryController:
    def create_category(self, data):
        CategoryModelObj = CategoryModel()
        functionsObj = functions()
        name, description = data.get('name'), data.get('description')
        if not name:
            return functionsObj.send_response(0, 'Missing name field')
        
        category = CategoryModelObj.create_category(name, description)
        return functionsObj.send_response(1, 'Category created successfully',category)
    
    def get_category(self, category_id):
        CategoryModelObj = CategoryModel()
        functionsObj = functions()
        category = CategoryModelObj.get_category_by_id(category_id)
        if not category:
            return functionsObj.send_response(0,'Category not found')
        
        return functionsObj.send_response(1, 'Category retrieved successfully',category)
    
    def get_all_categories(self):
        CategoryModelObj = CategoryModel()
        functionsObj = functions()
        categories = CategoryModelObj.get_all_categories()
        return functionsObj.send_response(1, 'Categories retrieved successfully',categories)
    
    def update_category(self, category_id, data):
        CategoryModelObj = CategoryModel()
        functionsObj = functions()
        if not data:
            return functionsObj.send_response(0,'No data found for updation')
        
        res = CategoryModelObj.update_category(category_id, **data)
        if res:
            return functionsObj.send_response(1, 'Category updated successfully')
        return functionsObj.send_response(0,'Category not found')
    
    def delete_category(self, category_id):
        CategoryModelObj = CategoryModel()
        functionsObj = functions()
        res = CategoryModelObj.delete_category(category_id)
        if res:
            return functionsObj.send_response(1,'Category deleted successfully')
        return functionsObj.send_response(0,'Category not found')
        