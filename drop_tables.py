import sqlite3

conn = sqlite3.connect('products.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE products
          ''')

conn.commit()
conn.close()
