
SELECT p.product_name
FROM order_item oi
JOIN product p ON oi.product_id = p.id
WHERE oi.order_id = 1;

SELECT p.*
FROM order_item oi
JOIN product p ON oi.product_id = p.id
WHERE oi.order_id = 2;



SELECT * from product where veg=True;