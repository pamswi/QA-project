import pytest
from flask import url_for
from flask_testing import TestCase
from application import app, db
from models import Product, BasketItem, Customer, Order, OrderItem


class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///testdata.db',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app
    
    def setUp(self):
        db.create_all()

        test_customer = Customer(
                first_name='John', 
                last_name='Doe', 
                email='john@example.com', 
                phone=1234567890, 
                address='123 Main St',
                card_number=1234567890123456, 
                card_expiry=('01/12/23'),
                card_cvc=123
                )
        
        db.session.add(test_customer)
        db.session.commit()

        
        test_pizzas = [
        Product(product_name='Margherita', description='Classic pizza with tomato sauce, mozzarella cheese, and basil.', price=10.99, img='margherita', veg=True, available=True),
        Product(product_name='Pepperoni', description='Pizza topped with tomato sauce, mozzarella cheese, and pepperoni slices.', price=12.99, img='pepperoni', veg=False, available=True),
        Product(product_name='Hawaiian', description='Pizza with tomato sauce, mozzarella cheese, ham, and pineapple.', price=11.99, img='hawaiian', veg=False, available=True),
        Product(product_name='Supreme', description='Loaded pizza with tomato sauce, mozzarella cheese, pepperoni, sausage, bell peppers, onions, and olives.', price=14.99, img='supreme', veg=False, available=True),
        Product(product_name='Veggie', description='Veggie pizza with tomato sauce, mozzarella cheese, bell peppers, onions, mushrooms, and olives.', price=11.99, img='veggie', veg=True, available=True),
        Product(product_name='Meat Lovers', description='For meat enthusiasts! Pizza with tomato sauce, mozzarella cheese, pepperoni, sausage, bacon, and ham.', price=13.99, img='meat_lovers', veg=False, available=True),
        Product(product_name='Mushroom', description='Pizza with tomato sauce, mozzarella cheese, and a generous topping of sliced mushrooms.', price=10.99, img='mushroom', veg=True, available=True),
        Product(product_name='BBQ Chicken', description='Tangy BBQ sauce, mozzarella cheese, grilled chicken, red onions, and cilantro on a pizza crust.', price=12.99, img='bbq_chicken', veg=False, available=True),
        Product(product_name='White Pizza', description='Creamy white sauce, mozzarella cheese, ricotta cheese, spinach, and garlic.', price=11.99, img='white_pizza', veg=True, available=True),
        Product(product_name='Buffalo Chicken', description='Spicy buffalo sauce, mozzarella cheese, grilled chicken, red onions, and a drizzle of ranch dressing.', price=12.99, img='buffalo_chicken', veg=False, available=True),
        Product(product_name='Pesto Delight', description='Pesto sauce, mozzarella cheese, sun-dried tomatoes, artichoke hearts, and feta cheese.', price=12.99, img='pesto_delight', veg=True, available=True),
        Product(product_name='Sausage and Onion', description='Pizza with tomato sauce, mozzarella cheese, Italian sausage, and caramelized onions.', price=11.99, img='sausage_onion', veg=False, available=True)
    ]
        db.session.add_all(test_pizzas)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_get(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)

    def test_menu_get(self):
        response = self.client.get(url_for('products'))
        self.assertEqual(response.status_code, 200)


    def test_contact_get(self):
        response = self.client.get(url_for('contact'))
        self.assertEqual(response.status_code, 200)

    def test_basket_get(self):
        response = self.client.get(url_for('basket'))
        self.assertEqual(response.status_code, 200)

    def test_checkout_get(self):
        response = self.client.get(url_for('checkout'))
        self.assertEqual(response.status_code, 200)

    def test_payment_get(self):
        response = self.client.get(url_for('payment', customer_id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Payment', response.data)

    def test_order_get(self):
        response = self.client.get(url_for('order', order_id=1))
        self.assertEqual(response.status_code, 200)
            

    def test_post_checkout(self):
        response = self.client.post(url_for('checkout'), data={
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane@example.com',
            'phone': '9876543210',
            'address': '456 Elm St'
        })

        self.assertEqual(response.status_code, 302)
        self.assertIn(b'/payment/2', response.data)      
            
            
    def test_post_basket(self):
        response = self.client.post(url_for('basket'), data={
            'product_id': '1',
            'remove_basket': 'Remove'
        })

        self.assertEqual(response.status_code, 302)
        self.assertIn(b'/basket', response.data)    

    def test_post_view_products(self):
        response = self.client.post(url_for('view_product', product='1'), data={
            'add_basket': '1'
        })

        self.assertEqual(response.status_code, 302)
        self.assertIn(b'/products/1', response.data)     
    
    def test_post_all_products(self):
        response = self.client.post(url_for('products'), data={
            'add_basket': '1'
        })

        self.assertEqual(response.status_code, 302)
        self.assertIn(b'/products', response.data)


    def test_post_payment(self):
        response = self.client.post(url_for('payment', customer_id=1), data={
            'card_number': '1234567890123456',
            'card_exp': '01/25',
            'card_cvv': '123',
            'success': 'success'
        })

        self.assertEqual(response.status_code, 302)
        self.assertIn(b'/success/1', response.data)