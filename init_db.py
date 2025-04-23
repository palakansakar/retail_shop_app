import sqlite3

# Connect to database (or create if it doesn't exist)
conn = sqlite3.connect('retailshop.db')

# Create a cursor
cursor = conn.cursor()

# Create a simple table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
''')

# Save and close
conn.commit()
conn.close()

print("Database initialized.")
