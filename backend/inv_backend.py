from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from model_mongodb import Product


app = Flask(__name__)

#CORS stands for Cross Origin Requests.
CORS(app) #Here we'll allow requests coming from any domain. Not recommended for production environment.

products = {
    'products_list' :
    [
        {
            'name' : 'couch',
            'price' : '-100',
            'quantity' : '1',
            'category' : 'furniture',
            'description' : 'dis a couch',
            'brand' : 'couch brand',
            'productID' : '420',
            'picture' : 'hi'
        }
    ]
}

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/products', methods=['GET', 'POST'])
def get_products():
    if request.method == 'GET':
        search_productName = request.args.get('name')
        if search_productName:
            result = Product().find_by_name(search_productName)
        else:
            result = Product().find_all()
        return {"products_list": result}
    elif request.method == 'POST':
        productToAdd = request.get_json()
        newProduct = Product(productToAdd)
        newProduct.save()
        resp = jsonify(newProduct), 201
        return resp

""" @app.route('/users/<id>', methods = ['DELETE'])
def get_user(id):
    if id:
        if request.method == 'DELETE':
            for user in users['users_list']:
                if user['id'] == id:
                    users['users_list'].remove(user)
        else:
            for user in users['users_list']:
                if user['id'] == id:
                    return user
            return ({})
    return users """