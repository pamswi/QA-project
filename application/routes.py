from application import app
from flask import render_template, request, flash, redirect
from models import Product, BasketItem

'''
the following .py file defines all known routes across the site
'''
@app.route('/')
def home():
   
    return render_template ('home.html')

@app.route('/aboutus')
def about():
    return render_template ('about.html')


@app.route('/basket', methods=["GET", "POST"])
def basket():
    products = BasketItem.all_basket()

    if request.method == "POST":
        if 'remove_basket' in request.form:
            id = request.form['product_id']
            print(id)
            BasketItem.remove_basket(id)
            return redirect('/basket')


    return render_template ('basket.html', products=products)

@app.route('/contactus')
def contact():
    return render_template ('contact.html')

@app.route('/checkout')
def checkout():
    return render_template ('checkout.html')

@app.route('/payment')
def payment():
    return render_template ('payment.html')

@app.route('/products', methods=["GET", "POST"])
def products():
    products = Product.all_products()


    if request.method == "POST":
        if 'product_details' in request.form:
            id = request.form['product_details']
        elif 'add_basket' in request.form:
            id = request.form['add_basket']
            BasketItem.add_to_basket(product_id=id)
            flash("item added to your basket")
    

    return render_template ('products.html', products=products)

@app.route('/products/veg')
def veg_products():
    products = Product.veg_products()

    if request.method == "POST":
        if 'product_details' in request.form:
            id = request.form['product_details']
        elif 'add_basket' in request.form:
            id = request.form['add_basket']
            BasketItem.add_to_basket(product_id=id)
            flash("item added to your basket")
            return redirect ('/products/veg')

    return render_template ('products.html', products=products) 

@app.route('/products/<product>')
def view_product(product):

    product = Product.product_by_id(product)
    
    return render_template ('product.html', product=product)

@app.route('/category')
def category():
    return render_template ('category.html')