from app import db, app, Customer, Product, Order, OrderItem

with app.app_context():
    db.drop_all()
    db.create_all()


    test_products = [
        Product(product_name='Product 1', description='Description 1', price=100),
        Product(product_name='Product 2', description='Description 2', price=150),
        Product(product_name='Product 3', description='Description 3', price=200),
    ]

    db.session.add_all(test_products)
    db.session.commit()

    test_customers = Customer(
            first_name='John', 
            last_name='Doe', 
            email='john@example.com', 
            phone=1234567890, 
            address='123 Main St',
            card_number=1234567890123456, 
            card_expiry=('12/23'),
            card_cvc=123
            )
    
    db.session.add(test_customers)
    db.session.commit()

    # test_order = Order(
    #     customer_id=1,
    #     order_date='10/08/2022',
    #     total_amount = 100
    #     )

    # db.session.add(test_order)
    # db.session.commit()

    # test_order_items = [
    #     OrderItem(
    #         order_id=2,
    #         product_id=1,
    #         quantity=1,
    #         subtotal=150
    #     ),
    #     OrderItem(
    #         order_id=2,
    #         product_id=2,
    #         quantity=1,
    #         subtotal=350
    #     )
    # ]
  
    # db.session.add_all(test_order_items)
    # db.session.commit()


    new_order = Order(
        customer_id=1,
        order_date='2023-08-10',
        total_amount=500
    )
    db.session.add(new_order)
    db.session.commit()
    # Create order items for the new order
    order_items = [
        OrderItem(
            order_id=new_order.id,
            product_id=1,
            quantity=2,
            subtotal=200
        ),
        OrderItem(
            order_id=new_order.id,
            product_id=2,
            quantity=1,
            subtotal=300
        )
    ]


    db.session.add_all(order_items)
    db.session.commit()


    new_order2 = Order(
        customer_id=1,
        order_date='2022-01-10',
        total_amount=500
    )
    db.session.add(new_order2)
    db.session.commit()

    # Create order items for the new order
    order_items2 = [
        OrderItem(
            order_id=new_order2.id,
            product_id=3,
            quantity=2,
            subtotal=200
        ),
        OrderItem(
            order_id=new_order2.id,
            product_id=1,
            quantity=1,
            subtotal=300
        )
    ]
    db.session.add_all(order_items2)
    db.session.commit()


    
    new_order3 = Order(
        customer_id=1,
        order_date='2000-01-10',
        total_amount=50
    )
    db.session.add(new_order3)
    db.session.commit()

    # Create order items for the new order
    order_items3 = [
        OrderItem(
            order_id=new_order3.id,
            product_id=3,
            quantity=1,
            subtotal=200
        ),
        OrderItem(
            order_id=new_order3.id,
            product_id=2,
            quantity=1,
            subtotal=300
        )
    ]
    db.session.add_all(order_items3)
    db.session.commit()

with app.app_context():
    products_for_order = (
        db.session.query(Product)
        .join(OrderItem, OrderItem.product_id == Product.id)
        .filter(OrderItem.order_id == 1)
        .all()
    )
for product in products_for_order:
    print(f"Product ID: {product.id}")
    print(f"Product Name: {product.product_name}")
    print(f"Description: {product.description}")
    print(f"Price: {product.price}")
    print(f"Available: {product.available}")
    print("----")