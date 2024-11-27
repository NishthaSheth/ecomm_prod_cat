from flask import Blueprint, request
from controllers.chemist_controller import ChemistController
from controllers.auth_controller import AuthController
from library.functions import jwt_required

chemist = Blueprint('chemist',__name__)

@chemist.route('/create',methods = ['POST'])
def create_chemist():
    data = request.json
    # ChemistControllerObj = ChemistController()
    return ChemistController.create_chemist(data)

@chemist.route('/login',methods = ['POST'])
def login():
    return AuthController.login()

@chemist.route('<string:email>', methods = ['GET'])
@jwt_required
def get_product(email):
    # ChemistControllerObj = ChemistController()
    return ChemistController.get_chemist_by_email(email)