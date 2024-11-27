from library.db import execute_query, insert

class CategoryModel:
    def create_category(self, name, description = None):
        data = {
            "name":name,
            "description":description
        }
        res = insert("categories",data)
        if res:
            cols = ['id','name','description']
            return dict(zip(cols, (res['category_id'], res['name'], res['description'])))
        return None
    
    def get_category_by_id(self, category_id):
        query = "SELECT * FROM categories WHERE category_id = %s;"
        params = (category_id,)
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
    
    def update_category(self, category_id, **kwargs):
        set_clause = ', '.join(f"{key} = %s" for key in kwargs.keys())
        params = tuple(kwargs.values()) + (category_id,)
        query = f"UPDATE categories SET {set_clause} WHERE category_id = %s;"
        res = execute_query(query, params)
        return res

    def delete_category(self, category_id):
        query = "DELETE FROM categories WHERE category_id = %s;"
        params = (category_id,)
        res = execute_query(query, params)
        return res
