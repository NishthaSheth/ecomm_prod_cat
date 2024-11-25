from flask import jsonify
from models.dbchemists import ChemistModel

class ChemistController:
    def create_chemist(data):
        name, email, phone = data.get('name'), data.get('email'), data.get('phone')
        if not all([name, email, phone]):
            return jsonify({'status_code':0, 'status_message':'Missing required parameters'}), 400
        
        chemist = ChemistModel.create_chemist(name, email, phone)
        return jsonify({'status_code':1, 'status_message':'Chemist created successfully', 'data': chemist})
    
    def authenticate_chemist(data):
        chemist_id, access_token = data.get('chemist_id'), data.get('access_token')
        if not ChemistModel.authenticate_chemist(chemist_id, access_token):
            return jsonify({'status_code':0, 'status_message':'Invalid credentials'}), 401
        return jsonify({'status_code':1, 'status_message':'Authenticated successfully'})