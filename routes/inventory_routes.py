from flask import Blueprint, request
from controllers.inventory_controller import InventoryController
from library.functions import jwt_required

inventory = Blueprint('inventory', __name__)

@inventory.route('/add', methods=['POST'])
@jwt_required
def add_inventory():
    data = request.json
    return InventoryController.add_inventory(data)

@inventory.route('/<int:inventory_id>', methods = ['GET'], endpoint = 'get_inv')
@jwt_required
def get_inventory(product_id):
    return InventoryController.get_inventory(product_id)

@inventory.route('/<int:inventory_id>', methods = ['PUT'], endpoint = 'update_inv')
@jwt_required
def update_inventory(inventory_id):
    data = request.json
    return InventoryController.update_inventory(inventory_id, data)

@inventory.route('/<int:inventory_id>', methods = ['DELETE'], endpoint = 'del_category')
@jwt_required
def delete_inventory(inventory_id):
    return InventoryController.delete_inventory(inventory_id)