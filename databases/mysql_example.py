import mysql.connector
conn = mysql.connector.connect(host="localhost", user="root", password="password")
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS example")
conn.close()