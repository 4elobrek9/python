import sqlite3

connection = sqlite3.connect('zoo.db')
cursor = connection.cursor()

cursor.execute("DELETE FROM animals WHERE name = 'Лев'")

cursor.execute("SELECT * FROM animals")
rows = cursor.fetchall()

connection.commit()

for row in rows:
    print(row)

connection.close()