from flask import jsonify
from models.inventory import InventoryModel

class InventoryController:
    def add_inventory(data):
        product_id, quantity, batch_number, expiry_date = (
            data.get('product_id'),
            data.get('quantity'),
            data.get('batch_number'),
            data.get('expiry_date')
        )

        if not all([product_id, quantity, batch_number, expiry_date]):
            return jsonify({'status_code':0,'status_message':'Missing required parameters'}),400
        
        inventory = InventoryModel.add_inventory(product_id, quantity, batch_number, expiry_date)
        return jsonify({'status_code':1, 'status_message':'Inventory added successfully','data':inventory})
    
    def get_inventory_by_product(product_id):
        inventory = InventoryModel.get_inventory_by_product(product_id)
        return jsonify({'status_code':1,'status_message':'Inventory retrieved successfully','data':inventory})
    
    def update_inventory(inventory_id, data):
        if not data:
            return jsonify({'status_code':0,'status_message':'No data found'}),400
        
        res = InventoryModel.update_inventory(inventory_id, **data)
        if res:
            return jsonify({'status_code':1,'status_message':'Inventory updated successfully'})
        return jsonify({'status_code':0, 'status_message':'Inventory ID not found'})
    
    def delete_inventory(inventory_id):
        res = InventoryModel.delete_inventory(inventory_id)
        if res:
            return jsonify({'status_code':1,'status_message':'Inventory deleted successfully'})
        return jsonify({'status_code':0,'status_message':'Inventory ID not found'})