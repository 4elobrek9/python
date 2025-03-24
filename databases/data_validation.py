import sqlite3
conn = sqlite3.connect("example.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE name IS NULL")
print("Invalid Data:", cursor.fetchall())
conn.close()