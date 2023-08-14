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
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()


    