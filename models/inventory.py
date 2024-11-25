from library.db import execute_query

class InventoryModel:
    def add_inventory(product_id, quantity, batch_number, expiry_date):
        query = """
            INSERT INTO inventory (product_id, quantity, batch_number, expiry_date, created_at)
            VALUES (:product_id, :quantity, :batch_number, :expiry_date, CURRENT_TIMESTAMP)
            RETURNING inventory_id, product_id, quantity, batch_number, expiry_date
        """
        params = {'product_id':product_id,'quantity':quantity,'batch_number':batch_number,'expiry_date':expiry_date}
        res = execute_query(query, params, fetch_one = True)
        if res:
            cols = ['inventory_id','product_id','quantity','batch_number','expiry_date']
            return dict(zip(cols, res))
        return None
    
    def get_inventory_by_product(product_id):
        query = "SELECT * FROM inventory WHERE product_id = :product_id"
        params = {'product_id':product_id}
        res = execute_query(query, params, fetch_all = True)
        if res:
            cols = ['inventory_id','product_id','quantity','batch_number','expiry_date']
            return dict(zip(cols, res))
        return None
    
    def update_inventory(inventory_id, **kwargs):
        set_clause = ', '.join(f"{key} = :{key}" for key in kwargs.keys())
        params = {**kwargs,'inventory_id':inventory_id}
        query = f"UPDATE inventory SET {set_clause} WHERE inventory_id = :inventory_id;"
        res = execute_query(query, params)
        return res

    def delete_inventory(inventory_id):
        query = "DELETE FROM inventory WHERE inventory_id = :inventory_id;"
        params = {'inventory_id':inventory_id}
        res = execute_query(query, params)
        return res