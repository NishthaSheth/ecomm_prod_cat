from flask import jsonify
from models.dbproducts import ProductModel

class ProductController:
    def create_product(data):
        required_fields = ['name','description','price','quantity','category_id']
        if not all(field in data for field in required_fields):
            return jsonify({'status_code':0, 'status_message':'Missing required parameters'}), 400
        
        product = ProductModel.create_product(data['name'], data['description'], data['price'], data['quantity'], data['category_id'])
        return jsonify({'status_code':1, 'status_message':'Product created successfully','data':product})
    
    def get_product_by_id(product_id):
        product = ProductModel.get_product_by_id(product_id)
        if product:
            return jsonify({'status_code':1, 'status_message':'Product retrieved successfully','data':product}),200
        
        return jsonify({'status_code':0,'status_message':'Product not found'}),404
    
    def update_product(product_id, data):
        if not data:
            return jsonify({'status_code':0,'status_message':'No data available'}),400
        
        res = ProductModel.update_product(product_id, **data)
        if res:
            return jsonify({'status_code':1,'status_message':'Product successfully updated'}),200
        return jsonify({'status_code':0,'status_message':'Product not found'}),404
    
    def delete_product(product_id):
        res = ProductModel.delete_product(product_id)
        if res:
            return jsonify({'status_code':1,'status_message':'Product successfully deleted'}),200
        return jsonify({'status_code':0,'status_message':'Product not found'}),404