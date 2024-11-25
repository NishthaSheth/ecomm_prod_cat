from library.db import execute_query

class CategoryModel:
    def create_category(name, description = None):
        query = """
            INSERT INTO categories (name, description, created_at) VALUES (:name, :description, CURRENT_TIMESTAMP)
            RETURNING category_id, name, description;
        """
        params = {'name': name, 'description': description}
        result = execute_query(query, params, fetch_one = True)
        if result:
            cols = ['id','name','description']
            return dict(zip(cols, result))
        return  None
    
    def get_category_by_id(category_id):
        query = "SELECT * FROM categories WHERE category_id = :category_id;"
        params = {'category_id': category_id}
        res = execute_query(query, params, fetch_one = True)
        if res:
            cols = ['name','description']
            return dict(zip(cols, res))
        return None
    
    def get_all_categories():
        query = "SELECT * FROM categories"
        res = execute_query(query, fetch_all = True)
        if res:
            cols = ['name','description']
            return dict(zip(cols, res))
        return None
    
    def update_category(category_id, **kwargs):
        set_clause = ', '.join(f"{key} = :{key}" for key in kwargs.keys())
        params = {**kwargs,'category_id':category_id}
        query = f"UPDATE categories SET {set_clause} WHERE category_id = :category_id;"
        res = execute_query(query, params)
        return res

    def delete_category(category_id):
        query = "DELETE FROM categories WHERE category_id = :category_id;"
        params = {'category_id':category_id}
        res = execute_query(query, params)
        return res
