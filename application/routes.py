from application import app
from flask import render_template, request, flash, redirect, url_for
from models import Product, BasketItem, Customer, Order, OrderItem
from datetime import date

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
    print(products)

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

@app.route('/checkout', methods=["GET", "POST"])
def checkout():
    products = BasketItem.all_basket()
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone  = request.form['phone']
        address = request.form['address']

        new_customer =Customer.add_customer(first_name, last_name, email, phone, address)
        return redirect (url_for('payment', customer_id=new_customer.id))


    return render_template ('checkout.html', products=products)

@app.route('/payment/<int:customer_id>', methods=["GET", "POST"])
def payment(customer_id):

    if request.method == "POST":
        card_number = request.form['card_number']
        card_expiry = request.form['card_exp']
        card_cvc = request.form['card_cvv']

        update_customer = Customer.add_payment(customer_id, card_number, card_expiry, card_cvc)

        if 'success' in request.form:
            basket_total = BasketItem.basket_total()
            new_order = Order.add_order(customer_id, date.today(), basket_total)            
            OrderItem.ordered_items(new_order.id)
            BasketItem.empty_basket()
            return redirect (url_for('success', customer_id=update_customer.id))
        
    return render_template ('payment.html', customer_id=customer_id)

@app.route('/success/<int:customer_id>')
def success(customer_id):

    past_orders=Order.past_orders(customer_id)

    return render_template('success.html', past_orders=past_orders)

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