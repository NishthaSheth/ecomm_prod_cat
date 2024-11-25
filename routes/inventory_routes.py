from flask import Blueprint, request
from controllers.inventory_controller import InventoryController

inventory = Blueprint('inventory', __name__)

@inventory.route('/add', methods=['POST'])
def add_inventory():
    data = request.json
    return InventoryController.add_inventory(data)

@inventory.route('/inventory/<int:inventory_id>', methods = ['GET'])
def get_inventory(product_id):
    return InventoryController.get_inventory(product_id)

@inventory.route('/<int:inventory_id>', methods = ['PUT'])
def update_inventory(inventory_id):
    data = request.json
    return InventoryController.update_inventory(inventory_id, data)

@inventory.route('/<int:inventory_id>', methods = ['DELETE'])
def delete_inventory(inventory_id):
    return InventoryController.delete_inventory(inventory_id)