from library.db import execute_query, insert

class ChemistModel:
    def create_chemist(self, name, email, phone, password):
        data = {
            "name": name,
            "email": email,
            "phone": phone,
            "password":password
        }
        print(data)
        res = insert("chemists", data)
        if res:
            cols = ['name','email','phone','password']
            return dict(zip(cols, (res['name'],res['email'],res['phone'],res['password'])))

    def get_chemist_by_email(email):
        query = "SELECT * FROM chemists WHERE email = %s;"
        params = (email,)
        return execute_query(query, params, fetch_one = True)