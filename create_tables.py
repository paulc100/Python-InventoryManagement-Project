import sqlite3

conn = sqlite3.connect('products.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE products
          (id INTEGER PRIMARY KEY ASC, 
           name VARCHAR(100) NOT NULL,
           price INTEGER,
           cost INTEGER,
           date_stocked VARCHAR(100),
           date_sold VARCHAR(100),
           is_sold INTEGER,
           camera VARCHAR(100),
           security VARCHAR(100),
           screen_body_ratio VARCHAR(100),
           graphics_card VARCHAR(100),
           "case" VARCHAR(100),
           memory_type VARCHAR(100),
           type VARCHAR(100))
          ''')

conn.commit()
conn.close()
