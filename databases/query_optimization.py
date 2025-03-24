import sqlite3
conn = sqlite3.connect("example.db")
cursor = conn.cursor()
cursor.execute("CREATE INDEX IF NOT EXISTS idx_name ON users (name)")
conn.close()