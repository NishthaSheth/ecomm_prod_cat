from models.dbproducts import ProductModel
from library.functions import functions

class ProductController:
    def create_product(data):
        ProductModelObj = ProductModel()
        functionsObj = functions()
        required_fields = ['name','description','price','quantity','category_id']
        if not all(field in data for field in required_fields):
            return functionsObj.send_response(0, 'Missing required parameters')
        
        product = ProductModelObj.create_product(data['name'], data['description'], data['price'], data['quantity'], data['category_id'])
        return functionsObj.send_response(1, 'Product created successfully',product)
    
    def get_product_by_id(self, product_id):
        ProductModelObj = ProductModel()
        functionsObj = functions()
        product = ProductModelObj.get_product_by_id(product_id)
        if product:
            return functionsObj.send_response(1, 'Product retrieved successfully', product)
        
        return functionsObj.send_response(0,'Product not found')
    
    def update_product(self, product_id, data):
        ProductModelObj = ProductModel()
        functionsObj = functions()
        if not data:
            return functionsObj.send_response(0,'No data available')
        
        res = ProductModelObj.update_product(product_id, **data)
        if res:
            return functionsObj.send_response(1,'Product successfully updated')
        return functionsObj.send_response(0, 'Product not found')
        
    def delete_product(self, product_id):
        ProductModelObj = ProductModel()
        functionsObj = functions()
        res = ProductModelObj.delete_product(product_id)
        if res:
            return functionsObj.send_response(1,'Product successfully deleted')
        return functionsObj.send_response(0,'Product not found')