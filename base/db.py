import sqlite3

connection = sqlite3.connect('zoo.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS animals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    age INTEGER
)       
''')

cursor.execute("INSERT INTO animals (name, species, age) VALUES ('Лев', 'Хищник', 5)")
cursor.execute("INSERT INTO animals (name, species, age) VALUES ('Слон', 'Млекопитающее', 19)")
cursor.execute("INSERT INTO animals (name, species, age) VALUES ('Попугай', 'Птица', 2)")

cursor.execute("SELECT * FROM animals")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.commit()
connection.close()
