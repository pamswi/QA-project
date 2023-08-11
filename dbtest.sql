
SELECT p.product_name
FROM order_item oi
JOIN product p ON oi.product_id = p.id
WHERE oi.order_id = 1;

SELECT p.*
FROM order_item oi
JOIN product p ON oi.product_id = p.id
WHERE oi.order_id = 2;



SELECT * from product where veg=True;

INSERT INTO basket_item (product_id, quantity) VALUES (?, ?)]
parameters: ('5', 1)

INSERT INTO order (customer_id, order_date, total_amount) VALUES ("5", "12/12/12", "11");

INSERT INTO orders(customer_id, order_date, total_amount)
VALUES (5, '2012-12-12', 11);
  
SELECT name FROM sqlite_master WHERE type = 'table';
