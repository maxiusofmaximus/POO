import mysql.connector
from tabulate import tabulate
connection = mysql.connector.connect(
    host="localhost", user="root", password="", database="biblioteca"
)
cursor = connection.cursor()

cursor.execute("SELECT * FROM libros")
datos = cursor.fetchall()

print(tabulate(datos, headers=[
      "ID", "TITULO", "AUTOR", "ISBN", "DISPONIBILIDAD"], tablefmt="pipe"))
