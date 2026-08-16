import sqlite3
import random
from datetime import date, timedelta

CATEGORIES = {
    'Electronics': ['Headphones', 'Smartphone', 'Laptop', 'Speaker'],
    'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Shoes'],
    'Grocery': ['Rice', 'Oil', 'Snacks', 'Beverages'],
    'Furniture': ['Chair', 'Table', 'Sofa', 'Bookshelf']
}
STORES = ['Delhi', 'Mumbai', 'Bangalore', 'Chennai']

def generate(db_path='data/sales.db', days=365, seed=42):
    random.seed(seed)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS sales')
    cur.execute('''
        CREATE TABLE sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sale_date TEXT,
            store TEXT,
            category TEXT,
            product TEXT,
            quantity INTEGER,
            unit_price REAL,
            revenue REAL
        )
    ''')
    start = date.today() - timedelta(days=days)
    rows = []
    for i in range(days):
        current_date = start + timedelta(days=i)
        for _ in range(random.randint(5, 15)):
            category = random.choice(list(CATEGORIES.keys()))
            product = random.choice(CATEGORIES[category])
            store = random.choice(STORES)
            quantity = random.randint(1, 10)
            unit_price = round(random.uniform(10, 500), 2)
            revenue = round(quantity * unit_price, 2)
            rows.append((current_date.isoformat(), store, category, product, quantity, unit_price, revenue))
    cur.executemany('''
        INSERT INTO sales (sale_date, store, category, product, quantity, unit_price, revenue)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', rows)
    conn.commit()
    conn.close()
    print(f'Inserted {len(rows)} rows into {db_path}')

if __name__ == '__main__':
    generate()
