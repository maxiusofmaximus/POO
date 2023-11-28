import mysql.connector
from tabulate import tabulate


class BaseDeDatos:

    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )
        self.cursor = self.connection.cursor()

    def ejecutar_sentencia(self, sentencia):
        self.cursor.execute(sentencia)
        self.connection.commit()

    def obtener_resultados(self, sentencia):
        self.cursor.execute(sentencia)
        return self.cursor.fetchall()


class Libro:

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponibilidad = True


class Biblioteca:

    def __init__(self, base_de_datos):
        self.base_de_datos = base_de_datos
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        sentencia = f"INSERT INTO libros (titulo, autor, isbn, disponibilidad) VALUES {(self.libros[0].titulo, self.libros[0].autor, self.libros[0].isbn, self.libros[0].disponibilidad)}"
        self.base_de_datos.ejecutar_sentencia(sentencia)

    def mostrar_libros_disponibles(self):
        sentencia = "SELECT * FROM libros"
        datos = self.base_de_datos.obtener_resultados(sentencia)
        print(tabulate(datos, headers=[
              "ID", "TITULO", "AUTOR", "ISBN", "DISPONIBILIDAD"], tablefmt="pipe"))

    def prestar_libros(self):
        sentencia = "SELECT * FROM libros WHERE disponibilidad = 1"
        datos = self.base_de_datos.obtener_resultados(sentencia)
        id_libro = int(input(
            "Ingrese el id del libro que desea prestar: "))
        for libro_en_biblioteca in datos:
            if libro_en_biblioteca[0] == id_libro:
                sentencia = f"UPDATE libros SET disponibilidad = 0 WHERE id = '{id_libro}'"
                base_de_datos.ejecutar_sentencia(sentencia)

    def devolver_libros(self):
        sentencia = "SELECT * FROM libros WHERE disponibilidad = 0"
        datos = self.base_de_datos.obtener_resultados(sentencia)
        id_libro = int(input(
            "Ingrese el id del libro que desea devolver: "))
        for libro_en_biblioteca in datos:
            if libro_en_biblioteca[0] == id_libro:
                sentencia = f"UPDATE libros SET disponibilidad = 1 WHERE id = '{id_libro}'"
                base_de_datos.ejecutar_sentencia(sentencia)


if __name__ == "__main__":
    base_de_datos = BaseDeDatos("localhost", "root", "1234", "biblioteca")
    biblioteca = Biblioteca(base_de_datos)

    while True:
        select = input("Ingrese la opción que desea realizar\n" +
                           "1. Agregar un libro a la biblioteca\n" +
                           "2. Eliminar un libro de la biblioteca\n" +
                           "3. Mostrar los libros de la biblioteca\n" +
                           "4. Prestar el libro\n" +
                           "5. Devolver el libro\n" +
                           "6. Salir del menú\n" +
                           "$ ")
        
        match select:
            case "1":
                libro = Libro(input("Ingrese el titulo del libro a agregar: "), input(
                    "Ingrese el autor del libro a agregar: "), input("Ingrese el ISBN del libro a agregar: "))
                
                biblioteca.agregar_libro(libro)

            case "2":
                id_libro = input("Ingrese el id del libro a eliminar: ")
                sentencia = f"DELETE FROM libros WHERE id = {id_libro}"
                base_de_datos.ejecutar_sentencia(sentencia)

            case "3":
                biblioteca.mostrar_libros_disponibles()

            case "4":
                biblioteca.prestar_libros()

            case "5":
                biblioteca.devolver_libros()

            case "6":
                print("Has salido del menú de opciones")
                break
            case _:
                print("Opción incorrectamente seleccionada")
