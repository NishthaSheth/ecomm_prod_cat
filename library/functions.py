from datetime import datetime, timedelta, timezone
import jwt
from flask import request
from dotenv import load_dotenv
import os

class functions:
    def send_response(self, status_code = "", status_message = "", data = ""):
        res = {}
        if status_code != "":
            res["status_code"] = status_code
        if status_message != "":
            res["status_message"] = status_message
        if data != "":
            res["data"] = data

        return res
    
    def generate_jwt_token(payload, expires_in = 3600):
        JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
        payload["exp"] = datetime.now(timezone.utc) + timedelta(seconds=expires_in)
        return jwt.encode(payload, JWT_SECRET_KEY, algorithm = 'HS256')
    
    def validate_jwt_token(jwt_token):
        JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
        try:
            return jwt.decode(jwt_token, JWT_SECRET_KEY, algorithms = ['HS256'])
        except jwt.ExpiredSignatureError:
            raise Exception('Token expired')
        except jwt.InvalidTokenError:
            raise Exception('Invalid token')
        
def jwt_required(f):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return functions.send_response(0,'Token missing!')
        
        try:
            token = token.split(" ")[0]
            payload = functions.validate_jwt_token(token)
        except Exception as e:
            return functions.send_response(0,str(e))
        
        request.user = payload
        return f(*args, **kwargs)
    
    return wrapper
    