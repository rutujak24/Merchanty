import json

# import flask modules
# Request - gets details for the request
# Flask - creates the flask app
from flask import Flask, request

# import flask_cors modules
# CORS - enable Cross Origin Resource Sharing
from flask_cors import CORS

# Connect to MongoDB
# from credentials import mongodb_parameters
# params = mongodb_parameters()
from pymongo import MongoClient
from bson import json_util

# Setup client and database
client = MongoClient('mongodb://localhost:27017')
db = client['test-database']

# Create the app and enable CORS
app = Flask(__name__)
CORS(app)

# Route at which the request is processed
# http://localhost:5000/products
@app.route('/products')
def products():

    cat = request.args.get('type')
    cursor = db.products.find({'type': cat})
    response = []
    for doc in cursor:
        doc.pop('_id', 0)
        response.append(doc)
    
    # Return json response
    response = json.dumps(response)
    return response

# http://localhost:5000/register
@app.route('/register')
def register():

    reg = {
        'name': request.args.get('name'),
        'uname': request.args.get('email'),
        'password': request.args.get('pass')
    }
    print(reg)

    db.login.insert_one(reg)
    # return 'Good'
    return app.send_static_file('login_page.html')

# http://localhost:5000/login
@app.route('/login')
def login():

    uname = request.args.get('email')
    password = request.args.get('pass')

    val = db.login.find_one({'uname': uname})
    
    if val == None:
        return 'Bad'
    
    if val['password'] == password:
        return 'Good'
    return 'Bad'

# http://localhost:5000/shipping
@app.route('/shipping')
def shipping():

    reg = {
        'uname': request.args.get('uname'),
        'name': request.args.get('name'),
        'email': request.args.get('email'),
        'contact': request.args.get('contact'),
        'address': request.args.get('address'),
        'zip': request.args.get('zip')
    }

    try:
        db.shipping.insert_one(reg)
        return 'Good'
    except:
        return 'Bad'

# http://localhost:5000/cart
@app.route('/cart')
def cart():

    print(request.args.get('price'))
    reg = {
        'uname': request.args.get('uname'),
        'item': request.args.get('item'),
        'type': request.args.get('type'),
        'price': request.args.get('price'),
        'image':request.args.get('image')
    }

    try:
        db.cart.insert_one(reg)
        return 'Success: Item added to cart'
    except:
        return 'Error: Item not added to cart'

@app.route('/')
def home():
    return 'Hello World'

@app.route('/usercart/<uname>')
def getUserCart(uname):
    matchedDocuments = db['cart'].find({"uname": str(uname)}, {"_id": 0, "item": 1, "type": 1, "price": 1, "image":1})
    # # matchedDocuments = list(matchedDocuments)
    # json.dumps(matchedDocuments)
    # print(type(matchedDocuments))
    # return matchedDocuments
    matchedDocumentsDict = {}
    i = 1
    for x in matchedDocuments:
        print(x)
        matchedDocumentsDict[i] = x
        i += 1
    return json.dumps(matchedDocumentsDict)

if __name__ == '__main__':
    app.run()