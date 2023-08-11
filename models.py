from application import db, app
from flask import session
from collections import Counter

'''
first we establish a connection with the shop database
the following code sets up a database consisting of 4 tables: customers, products, orders and order_items
'''

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(40))  # assuming email validation is handled elsewhere
    phone = db.Column(db.Integer)
    address = db.Column(db.String)
    card_number = db.Column(db.Integer)
    card_expiry = db.Column(db.String)
    card_cvc = db.Column(db.Integer)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(30))
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    img = db.Column(db.String)
    veg = db.Column(db.Boolean)
    available = db.Column(db.Boolean, default=True)

    @classmethod
    def product_by_id(cls, product_id):
        return cls.query.get(product_id)
    
    @classmethod
    def all_products(cls):
        return cls.query.all()

    @classmethod
    def veg_products(cls):
        return cls.query.filter_by(veg=True).all()

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column('customer_id', db.Integer, db.ForeignKey('customer.id'))
    order_date = db.Column(db.String)
    total_amount = db.Column(db.Integer)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column('order_id', db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column('product_id', db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer)
    subtotal = db.Column(db.Integer)


class BasketItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column('product_id', db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, default=1)
    
    @classmethod
    def add_to_basket(cls, product_id):
        new_item = BasketItem(product_id=product_id)
        with app.app_context():
            db.session.add(new_item)
            db.session.commit()
        return new_item

    @classmethod
    def all_basket(cls):
        basket_items = cls.query.all()
        product_counts = Counter(item.product_id for item in basket_items)
        products = Product.query.filter(Product.id.in_(product_counts.keys())).all()
        products_with_counts = [(product, product_counts[product.id]) for product in products]
        
        return products_with_counts
    

    @classmethod
    def remove_basket(cls, product_id):
        with app.app_context():
            product = Product.query.get(product_id)

            if product:
                # Get the basket item for the product
                basket_item = BasketItem.query.filter_by(product_id=product_id).first()

                if basket_item:
                    # If quantity is more than 1, reduce quantity by one
                    if basket_item.quantity > 1:
                        basket_item.quantity -= 1
                    else:
                        # If quantity is 1, remove the item from the basket
                        db.session.delete(basket_item)

                    db.session.commit()
                    return "Item removed from the basket."
                else:
                    return "Item not found in the basket."
            else:
                return "Product not found."