from library.db import execute_query

class ProductModel:
    def create_product(name, description, price, quantity, category_id):
        query = """
            INSERT INTO products(name, description, price, quantity, category_id, created_at) VALUES (:name, :description, :price, :quantity, :category_id, CURRENT_TIMESTAMP)
            RETURNING product_id, name, price;
        """
        params = {
            'name':name,
            'description':description,
            'price':price,
            'quantity':quantity,
            'category_id':category_id
        }
        result = execute_query(query, params, fetch_one = True)
        if result:
            columns = ['id','name','price']
            return dict(zip(columns, result))
        return None
    
    def get_product_by_id(product_id):
        query = "SELECT * FROM products WHERE product_id = :product_id;"
        params = {'product_id':product_id}

        result = execute_query(query, params, fetch_one = True)
        if result:
            columns = ['name','description','price','category_id']
            return dict(zip(columns, result))
        return None
    
    def update_product(product_id, **kwargs):
        set_clause = ', '.join([f"{key} = :{key}" for key in kwargs.keys()])
        params = {**kwargs,'product_id':product_id}
        query = f"UPDATE products SET {set_clause} WHERE product_id = :product_id;"
        res = execute_query(query, params)
        return res

    def delete_product(product_id):
        query = "DELETE FROM products WHERE product_id = :product_id;"
        params = {'product_id': product_id}
        res = execute_query(query, params)
        return res