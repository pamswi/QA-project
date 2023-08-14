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
    phone = db.Column(db.String(20))
    address = db.Column(db.String(255))
    card_number = db.Column(db.String(20))
    card_expiry = db.Column(db.String(10))
    card_cvc = db.Column(db.Integer)

    @classmethod
    def add_customer(cls, first_name, last_name, email, phone, address):
        new_customer = Customer(first_name=first_name, last_name=last_name, email=email, phone=phone,address=address)
        db.session.add(new_customer)
        db.session.commit()
        return new_customer
    # retrieve customer entry to add remaining details
    @classmethod
    def add_payment(cls, customer_id, card_number, card_expiry, card_cvc):
        customer = cls.query.get(customer_id)

        if customer:
            customer.card_number = card_number
            customer.card_expiry = card_expiry 
            customer.card_cvc = card_cvc
            db.session.commit()
            return customer
        else:
            return "customer not found"

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(30))
    description = db.Column(db.String(1000))
    price = db.Column(db.Integer)
    img = db.Column(db.String(200))
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
    order_date = db.Column(db.String(15))
    total_amount = db.Column(db.Integer)

    items = db.relationship('OrderItem', backref='order', lazy=True)


    @classmethod
    def add_order(cls, customer_id, order_date, total_amount):
        new_order=Order(customer_id=customer_id,order_date=order_date, total_amount=total_amount)
        db.session.add(new_order)
        db.session.commit()
        return new_order
    
    @classmethod
    def past_orders(cls, customer_id):
        past_orders = cls.query.filter_by(customer_id=customer_id).all()
        return past_orders
    
    @classmethod
    def last_order(cls, customer_id):
        last_order = cls.query.filter_by(customer_id=customer_id).order_by(cls.id.desc()).first()
        return last_order
    
    @classmethod
    def specific_order(cls, order_id):
        order = cls.query.filter_by(id=order_id).first()
        return order


class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column('order_id', db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column('product_id', db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer)
    subtotal = db.Column(db.Integer)

    @classmethod
    def ordered_items(cls, order_id):
        basket = BasketItem.all_basket()
        for item, quantity in basket:
            subtotal = quantity * item.price
            new_item = OrderItem(order_id=order_id, product_id=item.id, quantity=quantity, subtotal=subtotal)
            db.session.add(new_item)
        db.session.commit()

        
class BasketItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column('product_id', db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, default=1)

    product = db.relationship('Product', backref='basket_items')
    
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
    def basket_total(cls):
        basket_items = cls.query.all()
        total_cost = sum(item.product.price * item.quantity for item in basket_items)
        return total_cost
    
    @classmethod
    def empty_basket(cls):
        cls.query.delete()
        db.session.commit()
    

    @classmethod
    def remove_basket(cls, product_id):
        with app.app_context():
            product = Product.query.get(product_id)

            if product:
                basket_item = BasketItem.query.filter_by(product_id=product_id).first()
                if basket_item:
                    if basket_item.quantity > 1:
                        basket_item.quantity -= 1
                    else:
                        db.session.delete(basket_item)
                    db.session.commit()
                    return "Item removed from the basket."
                else:
                    return "Item not found in the basket."
            else:
                return "Product not found."
            

