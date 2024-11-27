from library.db import execute_query, insert

class InventoryModel:
    def add_inventory(self, product_id, quantity, batch_number, expiry_date):
        data = {
            "product_id": product_id,
            "quantity": quantity,
            "batch_number": batch_number,
            "expiry_date":expiry_date
        }
        res = insert("inventory", data)
        if res:
            cols = ['inventory_id','product_id','quantity','batch_number','expiry_date']
            return dict(zip(cols, (res['inventory_id'],res['product_id'],res['quantity'],res['batch_number'],res['expiry_date'])))
    
    def get_inventory_by_product(self, product_id):
        query = "SELECT * FROM inventory WHERE product_id = %s;"
        params = (product_id,)
        res = execute_query(query, params, fetch_all = True)
        if res:
            cols = ['inventory_id','product_id','quantity','batch_number','expiry_date']
            return dict(zip(cols, res))
        return None
    
    def update_inventory(self, inventory_id, **kwargs):
        set_clause = ', '.join(f"{key} = %s" for key in kwargs.keys())
        params = tuple(kwargs.values()) + (inventory_id,)
        query = f"UPDATE inventory SET {set_clause} WHERE inventory_id = %s;"
        res = execute_query(query, params)
        return res

    def delete_inventory(self, inventory_id):
        query = "DELETE FROM inventory WHERE inventory_id = :inventory_id;"
        params = {'inventory_id':inventory_id}
        res = execute_query(query, params)
        return res