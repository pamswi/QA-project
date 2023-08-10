from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from application import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

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
    available = db.Column(db.Boolean, default=True)

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


import requests

url = "https://pizza-and-desserts.p.rapidapi.com/pizzas"

headers = {
	"X-RapidAPI-Key": "c0e4c58490mshd9e88fc7b6a083fp11049ajsn60ece8d68db4",
	"X-RapidAPI-Host": "pizza-and-desserts.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())








if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')