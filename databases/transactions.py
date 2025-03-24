import sqlite3
conn = sqlite3.connect("example.db")
cursor = conn.cursor()
try:
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Bob",))
    conn.commit()
except:
    conn.rollback()
finally:
    conn.close()