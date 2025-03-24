import sqlite3
conn = sqlite3.connect("example.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS new_users (id INTEGER PRIMARY KEY, name TEXT)"
cursor.execute("INSERT INTO new_users SELECT * FROM users")
conn.commit()
conn.close()