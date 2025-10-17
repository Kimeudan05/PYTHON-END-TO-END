from database import db

class Product(db.Model): # db.model is the SQLAlchemy ORM base
    __tablename__ = "products"

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable=False)
    category = db.Column(db.String(50))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    
    def __repr__(self):
        return f"<Product(id={self.id},name={self.name}, price ={self.price})>"
    
    # a function to convert the input to dictionary
    def to_dict(self):
        return{
            "id":self.id,
            "name":self.name,
            "category":self.category,
            "price":self.price,
            "quantity":self.quantity
        }