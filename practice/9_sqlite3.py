import sqlite3

# create a connection (if naot available, it creates a new database)
conn = sqlite3.connect('ecommerce.db')

# create a cursor
cur = conn.cursor()
print("connected to database successifully")

# create tables (customers and orders)
cur.execute("""
CREATE TABLE IF NOT EXISTS customers(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    email TEXT UNIQUE,
    city TEXT,
    region TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    order_date TEXT,
    product_name TEXT,
    quantity INTEGER CHECK(quantity > 0),
    price REAL,
    status TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);
""")

conn.commit()
print("✅ Tables created successfully!")

# insert data
customers = [
    ("Daniel", "Masila", "daniel@example.com", "Nairobi", "Central"),
    ("Jane", "Mwangi", "jane@example.com", "Nakuru", "Rift Valley"),
    ("John", "Otieno", "john@example.com", "Kisumu", "Western")
]

cur.executemany(
    """
    INSERT INTO customers (first_name,last_name,email,city,region)
    VALUES (?,?,?,?,?)
    """,customers
)

orders = [
    (1, "2025-10-01", "Wireless Mouse", 2, 1200, "Delivered"),
    (2, "2025-10-03", "Laptop Stand", 1, 3500, "Shipped"),
    (3, "2025-10-07", "HDMI Cable", 3, 800, "Pending")
]

cur.executemany("""
INSERT INTO orders (customer_id, order_date, product_name, quantity, price, status)
VALUES (?, ?, ?, ?, ?, ?)
""", orders)

conn.commit()
print("✅ Data inserted!")