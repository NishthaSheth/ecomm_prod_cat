from library.db import execute_query, insert

class ProductModel:
    def create_product(self, name, description, price, quantity, category_id):
        data = {
            "name": name,
            "description": description,
            "price": price,
            "quantity": quantity,
            "category_id": category_id
        }
        res = insert("products",data)
        if res:
            cols = ['name','price']
            return dict(zip(cols, (res['name'],res['price'])))
        return None
    
    def get_product_by_id(self, product_id):
        query = "SELECT * FROM products WHERE product_id = %s;"
        params = (product_id)

        result = execute_query(query, params, fetch_one = True)
        if result:
            columns = ['name','description','price','category_id']
            return dict(zip(columns, result))
        return None
    
    def update_product(self, product_id, **kwargs):
        set_clause = ', '.join([f"{key} = %s" for key in kwargs.keys()])
        params = tuple(kwargs.values())+(product_id,)
        query = f"UPDATE products SET {set_clause} WHERE product_id = %s;"
        res = execute_query(query, params)
        return res

    def delete_product(self, product_id):
        query = "DELETE FROM products WHERE product_id = %s;"
        params = (product_id,)
        res = execute_query(query, params)
        return res