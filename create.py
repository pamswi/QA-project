from application import db, app
from models import Product, Customer, Order, OrderItem


with app.app_context():
    db.drop_all()
    db.create_all()


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


#     test_customers = Customer(
#             first_name='John', 
#             last_name='Doe', 
#             email='john@example.com', 
#             phone=1234567890, 
#             address='123 Main St',
#             card_number=1234567890123456, 
#             card_expiry=('12/23'),
#             card_cvc=123
#             )
    
#     db.session.add(test_customers)
#     db.session.commit()

#     test_order = Order(
#         customer_id=1,
#         order_date='10/08/2022',
#         total_amount = 100
#         )

#     db.session.add(test_order)
#     db.session.commit()

#     test_order_items = [
#         OrderItem(
#             order_id=1,
#             product_id=1,
#             quantity=1,
#             subtotal=150
#         ),
#         OrderItem(
#             order_id=1,
#             product_id=2,
#             quantity=1,
#             subtotal=350
#         )
#     ]
  
#     db.session.add_all(test_order_items)
#     db.session.commit()


#     # new_order = Order(
#     #     customer_id=1,
#     #     order_date='2023-08-10',
#     #     total_amount=500
#     # )
#     # db.session.add(new_order)

#     # db.session.commit()
#     # # Create order items for the new order
#     # order_items = [
#     #     OrderItem(
#     #         order_id=new_order.id,
#     #         product_id=1,
#     #         quantity=2,
#     #         subtotal=200
#     #     ),
#     #     OrderItem(
#     #         order_id=new_order.id,
#     #         product_id=2,
#     #         quantity=1,
#     #         subtotal=300
#     #     )
#     # ]


#     # db.session.add_all(order_items)
#     # db.session.commit()


# #     new_order2 = Order(
# #         customer_id=1,
# #         order_date='2022-01-10',
# #         total_amount=500
# #     )
# #     db.session.add(new_order2)
# #     db.session.commit()

# #     # Create order items for the new order
# #     order_items2 = [
# #         OrderItem(
# #             order_id=new_order2.id,
# #             product_id=3,
# #             quantity=2,
# #             subtotal=200
# #         ),
# #         OrderItem(
# #             order_id=new_order2.id,
# #             product_id=1,
# #             quantity=1,
# #             subtotal=300
# #         )
# #     ]
# #     db.session.add_all(order_items2)
# #     db.session.commit()


    
# #     new_order3 = Order(
# #         customer_id=1,
# #         order_date='2000-01-10',
# #         total_amount=50
# #     )
# #     db.session.add(new_order3)
# #     db.session.commit()

# #     # Create order items for the new order
# #     order_items3 = [
# #         OrderItem(
# #             order_id=new_order3.id,
# #             product_id=3,
# #             quantity=1,
#             subtotal=200
#         ),
#         OrderItem(
#             order_id=new_order3.id,
#             product_id=2,
#             quantity=1,
#             subtotal=300
#         )
#     ]
#     db.session.add_all(order_items3)
#     db.session.commit()

# with app.app_context():
#     products_for_order = (
#         db.session.query(Product)
#         .join(OrderItem, OrderItem.product_id == Product.id)
#         .filter(OrderItem.order_id == 1)
#         .all()
#     )
# for product in products_for_order:
#     print(f"Product ID: {product.id}")
#     print(f"Product Name: {product.product_name}")
#     print(f"Description: {product.description}")
#     print(f"Price: {product.price}")
#     print(f"Available: {product.available}")
#     print("----")