import sqlite3

# Connect to the database (or create if it doesn't exist)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create a users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
""")

# Insert sample data
cursor.execute("INSERT INTO users (name, email) VALUES ('Ankita Gupta', 'ankitag@maqsoftware.com')")

# Commit and close
conn.commit()
conn.close()

print("Database and table created successfully!")
