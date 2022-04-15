from ecommerceapp import db

class Product(db.Model):
    # write your code here
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), nullable=False)
    products = db.relationship('CartProduct', backref='product', lazy=True)
    
class Category(db.Model):
    # write your code here
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100), nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)

class Cart(db.Model):
    # write your code here
    cart_id = db.Column(db.Integer, primary_key=True)
    total_amount = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    carts = db.relationship('CartProduct', backref='cart', lazy=True)
   
class CartProduct(db.Model):
    # write your code here
    cp_id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.cart_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))

class Role(db.Model):
    # write your code here
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), nullable=False)
    users = db.relationship('User', backref='role')

class User(db.Model):
    # write your code here
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    user_role = db.Column(db.Integer, db.ForeignKey('role.role_id'))
    carts = db.relationship('Cart', backref='user')
    products = db.relationship('Product', backref='user')
