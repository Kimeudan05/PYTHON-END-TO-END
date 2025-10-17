from flask import Flask,render_template,request,jsonify
from database import init_db,db
from models import Product
from flasgger import Swagger

# automatic flask api docs
app = Flask(__name__)
Swagger(app)

init_db(app) # connects the flask to postgreSQL database

# create tables on startup
with app.app_context():
    db.create_all()

# @app.route(...) =>  # defines the API endpoints

# home route
@app.route("/") 
def hello():
    return jsonify({"message":"Welcome to Flask API"})

# get all products
@app.route("/api/products",methods =['GET'])
def get_products():
    """
    Get all products
    ---
    responses:
      200:
        description: A list of products
        schema:
          type: array
          items:
            properties:
              id:
                type: integer
                example: 1
              name:
                type: string
                example: Laptop
              category:
                type: string
                example: Electronics
              price:
                type: number
                example: 999.99
              quantity:
                type: integer
                example: 5
    """
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])

# get a single product using an id
@app.route("/api/products/<int:product_id>",methods=["GET"])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error":"Product not found"}),404
    return jsonify(product.to_dict())

# create new product
@app.route("/api/products",methods =["POST"])
def add_products():
    """
    Add a new product
    ---
    parameters:
      - in: body
        name: body
        schema:
          required:
            - name
          properties:
            name:
              type: string
              example: "iPhone 16"
            category:
              type: string
              example: "Electronics"
            price:
              type: number
              example: 1450.99
            quantity:
              type: integer
              example: 12
    responses:
      201:
        description: Product added successfully
      400:
        description: Invalid input
    """
    data =request.get_json() # reads clients input
    try:
        product  = Product(
            name=data["name"],
            category = data.get("category"),
            price = data.get("price",0),
            quantity = data.get("quantity",0)
        )
        db.session.add(product)
        db.session.commit() # save changes
        return jsonify({"message":"Product added successifully"}),201 # jsonify return s clients API responses
    
    except Exception as e:
        db.session.rollback() #Prevents crashes on errors
        return jsonify({"error":str(e)}),400
    
# update a product
@app.route("/api/products/<int:product_id>",methods=["PUT"])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error":"Product not found"}),404
    
    data = request.get_json()
    product.name = data.get("name",product.name)
    product.category = data.get("category",product.category)
    product.price = data.get("price",product.price)
    product.quantity = data.get("quantity",product.quantity)
    
    db.session.commit()
    return jsonify({"message":"Product updated ","product":product.to_dict()})

# Delete a product
@app.route("/api/products/<int:product_id>",methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error":"Product not found"}),404
    
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message":f"Product ID {product_id} deleted successifully"})


# an example of a different route
@app.route("/about")
def about():
    return "This is my first flask app"

if __name__ == "__main__":
    app.run(debug=True)