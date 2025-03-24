import sqlite3
conn = sqlite3.connect("example.db")
cursor = conn.cursor()
cursor.execute("VACUUM INTO 'backup.db'")
conn.close()