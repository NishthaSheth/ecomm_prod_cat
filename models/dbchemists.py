import random
import string
from library.db import execute_query

class ChemistModel:
    def generate_access_token():
        return ''.join(random.choices(string.ascii_letters + string.digits, k = 10))
    
    def create_chemist(name, email, phone):
        access_token = ChemistModel.generate_access_token()
        query = """
            INSERT INTO chemists (name, email, phone, access_token, created_at)
            VALUES (:name, :email, :phone, :access_token, CURRENT_TIMESTAMP)
            RETURNING chemist_id, name, email, access_token;
        """
        params = {
            "name":name,
            "email":email,
            "phone":phone,
            "access_token":access_token
        }

        result = execute_query(query, params, fetch_one = True)
        if result:
            columns = ['chemist_id','name','email']
            return dict(zip(columns, result))
        return None
    
    def get_chemist_by_id(chemist_id):
        query = "SELECT * FROM chemists WHERE chemist_id = :chemist_id;"
        params = {'chemist_id':chemist_id}
        return execute_query(query, params, fetch_one = True)
    
    def authenticate_chemist(chemist_id, access_token):
        query = "SELECT * FROM chemists WHERE chemist_id = :chemist_id AND access_token = :access_token;"
        params = {'chemist_id':chemist_id, 'access_token': access_token}
        return execute_query(query, params, fetch_one = True) is not None