import mysql.connector
connection = mysql.connector.connect(
    host="localhost", user="root", password="", database="biblioteca"
)
cursor = connection.cursor()

cursor.execute("SELECT * FROM libros")
datos = cursor.fetchall()

for i in datos:
    print(*i)
