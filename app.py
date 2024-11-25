from flask import Flask
from routes.chemist_routes import chemist
from routes.product_routes import product
from routes.category_routes import category
from routes.inventory_routes import inventory
from library.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:admin@localhost/prod_cat'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(chemist, url_prefix = '/chemist')
app.register_blueprint(product, url_prefix = '/product')
app.register_blueprint(category, url_prefix = '/category')
app.register_blueprint(inventory, url_prefix = '/inventory')

if __name__ == '__main__':
    app.run(debug = True)