---- CREATIG TABLES AND INSERTING DATA IN THE DATABASE ---
CREATE TABLE  IF NOT EXISTS customers(
    customer_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(100) ,
    last_name VARCHAR(100) ,
    email VARCHAR(100) unique,
    city VARCHAR(100),
    region VARCHAR(100),
    created_at DATE DEFAULT CURRENT_TIMESTAMP
);

SELECT * from customers;

CREATE TABLE IF NOT EXISTS orders(
    order_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    product_name TEXT,
    quantity INT CHECK (quantity>0),
    price DECIMAL (10,2),
    status VARCHAR(50),
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);


-- ✅ Insert Customers
INSERT INTO customers (first_name,last_name,email,city,region)
VALUES
 ('Jane','Mwangi','jane.mwangi@example.com','Nakuru','Rift Valley'),
 ('John','Otieno','john.otieno@example.com','Kisumu','Western'),
 ('Mary','Wambui','mary.wambui@example.com','Thika','Central'),
 ('Brian','Ochieng','brian.ochieng@example.com','Eldoret','Rift Valley'),
 ('Lucy','Kamau','lucy.kamau@example.com','Mombasa','Coast');
 ('Masila','Kionzo','masila.kilonzo@example.com','Nairobi','Central');

-- ✅ Insert Orders
INSERT INTO orders (customer_id,order_date,product_name,quantity,price,status)
VALUES
 (1,'2025-10-01','Wireless Mouse',2,1200,'Delivered'),
 (1,'2025-10-03','USB Keyboard',1,2000,'Shipped'),
 (2,'2025-10-05','Laptop Stand',1,3500,'Delivered'),
 (3,'2025-10-07','HDMI Cable',3,800,'Pending'),
 (4,'2025-10-09','Monitor 24 inch',1,16000,'Delivered'),
 (5,'2025-10-10','Office Chair',1,18000,'Processing'),
 (3,'2025-10-11','Desk Lamp',2,2500,'Delivered');


--- LOOKING AT THE DATA AND DOING BASIC ANALYSIS
-- Read all customers with their orders
SELECT 
    c.first_name,
    c.last_name,
    c.first_name || ' ' || c.last_name AS name,
    o.order_id,
    o.product_name,
    o.status 
FROM customers c 
LEFT JOIN orders o 
ON c.customer_id = o.customer_id;

-- UPDATE : mark an order as delivered
UPDATE orders
SET status ='Delivered'
WHERE order_id =4;

-- DELETE : remove cancelled orders
DELETE FROM orders
WHERE status = 'Cancelled';

-- JOINS

-- INNER JOIN :only customers who made orders
SELECT c.customer_id,c.first_name,c.last_name,o.product_name,o.quantity
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;

-- LEFT JOIN : all customers , even without orders
SELECT c.customer_id,c.first_name,c.last_name,o.product_name,o.quantity
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id;

-- Aggregation : total spent per customer
SELECT c.first_name || ' ' || c.last_name AS name, SUM(o.price * o.quantity) AS total_spent 
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY total_spent DESC;

-- CREATING INDEXES
CREATE INDEX idx_customer_email ON customers(email);
CREATE INDEX idx_customer_id ON customers(customer_id);
CREATE INDEX idx_order_date ON orders(order_date);

-- ANALYTICS QUERIES

-- most popular product
SELECT product_name,COUNT(order_id) AS total_orders 
FROM orders
GROUP BY product_name
ORDER BY total_orders DESC;

-- Montly sales summary
SELECT DATE_TRUNC('month',order_date) AS month,
    SUM(price* quantity)
FROM orders
GROUP BY month
ORDER BY month;

-- Total customers by region
SELECT region,COUNT(*) AS total_customers FROM customers
GROUP BY region
ORDER BY total_customers DESC;