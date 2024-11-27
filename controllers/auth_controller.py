from flask import request
from werkzeug.security import check_password_hash
from models.dbchemists import ChemistModel
from library.functions import functions

class AuthController:
    def login():
        functionsObj = functions()
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return functionsObj.send_response(0,'Email and Password are required')
        
        chemist = ChemistModel.get_chemist_by_email(email)
        if not chemist or not check_password_hash(chemist['password'], password):
            return functionsObj.send_response(0,'Invalid credentials')
        
        payload = {'email':email}
        token = functions.generate_jwt_token(payload)

        return functionsObj.send_response(1,'Login successful',token)