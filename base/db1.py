import sqlite3

connection = sqlite3.connect('zoo.db')
cursor = connection.cursor()

cursor.execute("UPDATE animals SET age = 8 WHERE name = 'Лев'")

cursor.execute("SELECT * FROM animals")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.commit()
connection.close()