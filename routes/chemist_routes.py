from flask import Blueprint, request
from controllers.chemist_controller import ChemistController

chemist = Blueprint('chemist',__name__)

@chemist.route('/create',methods = ['POST'])
def create_chemist():
    data = request.json
    return ChemistController.create_chemist(data)

@chemist.route('/authenticate',methods = ['POST'])
def authenticate_chemist():
    data = request.json
    return ChemistController.authenticate_chemist(data)

