from models.inventory import InventoryModel
from library.functions import functions

class InventoryController:
    def add_inventory(self, data):
        InventoryModelObj = InventoryModel()
        functionsObj = functions()
        product_id, quantity, batch_number, expiry_date = (
            data.get('product_id'),
            data.get('quantity'),
            data.get('batch_number'),
            data.get('expiry_date')
        )

        if not all([product_id, quantity, batch_number, expiry_date]):
            return functionsObj.send_response(0,'Missing required parameters')
        
        inventory = InventoryModelObj.add_inventory(product_id, quantity, batch_number, expiry_date)
        return functionsObj.send_response(1, 'Inventory added successfully',inventory)
    
    def get_inventory_by_product(self, product_id):
        InventoryModelObj = InventoryModel()
        functionsObj = functions()
        inventory = InventoryModelObj.get_inventory_by_product(product_id)
        return functionsObj.send_response(1,'Inventory retrieved successfully',inventory)
    
    def update_inventory(self, inventory_id, data):
        InventoryModelObj = InventoryModel()
        functionsObj = functions()
        if not data:
            return functionsObj.send_response(0,'No data found')
        
        res = InventoryModelObj.update_inventory(inventory_id, **data)
        if res:
            return functionsObj.send_response(1,'Inventory updated successfully')
        return functionsObj.send_response(0, 'Inventory ID not found')
    
    def delete_inventory(self, inventory_id):
        InventoryModelObj = InventoryModel()
        functionsObj = functions()
        res = InventoryModelObj.delete_inventory(inventory_id)
        if res:
            return functionsObj.send_response(1,'Inventory deleted successfully')
        return functionsObj.send_response(0,'Inventory ID not found')