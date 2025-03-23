import sqlite3

connection = sqlite3.connect('zoo.db')
cursor = connection.cursor()

# cursor.execute("ALTER TABLE animals ADD COLUMN room INTEGER")

cursor.execute("INSERT INTO animals (name, species, age, room) VALUES ('Лев', 'Хищник', 5, 25)")

cursor.execute("SELECT * FROM animals")
rows = cursor.fetchall()

connection.commit()

for row in rows:
    print(*row)

connection.close()