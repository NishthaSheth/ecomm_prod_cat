from models.dbchemists import ChemistModel
from library.functions import functions
from werkzeug.security import generate_password_hash

class ChemistController:
    def create_chemist(self, data):
        ChemistModelObj = ChemistModel()
        functionsObj = functions()
        name, email, phone, password = data.get('name'), data.get('email'), data.get('phone'), data.get('password')
        if not all([name, email, phone, password]):
            return functionsObj.send_response(0, 'Missing required parameters')
        
        hashed_password = generate_password_hash(password)
        
        chemist = ChemistModelObj.create_chemist(name, email, phone, hashed_password)
        return functionsObj.send_response(1, 'Chemist created successfully', chemist)
    
    def get_chemist_by_email(self, email):
        ChemistModelObj = ChemistModel()
        functionsObj = functions()
        chemist = ChemistModelObj.get_chemist_by_email(email)
        if chemist:
            return functionsObj.send_response(1, 'Chemist retrieved successfully', chemist)
        return functionsObj.send_response(0,'Chemist not found')