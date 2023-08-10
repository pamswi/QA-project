from application import app
from flask import render_template

'''
the following .py file defines all known routes across the site
'''
@app.route('/')
def home():
    return render_template ('home.html')

@app.route('/aboutus')
def about():
    return render_template ('about.html')


@app.route('/basket')
def basket():
    return render_template ('basket.html')

@app.route('/contactus')
def contact():
    return render_template ('contact.html')

@app.route('/checkout')
def checkout():
    return render_template ('checkout.html')

@app.route('/payment')
def payment():
    return render_template ('payment.html')

@app.route('/products')
def products():
    return render_template ('products.html')

@app.route('/products/<product>')
def view_product(product):
    return render_template ('product.html')

@app.route('/category')
def category():
    return render_template ('category.html')