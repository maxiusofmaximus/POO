import mysql.connector


class Libro:

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponibilidad = True

    def prestar(self):
        self.disponibilidad = False


class Biblioteca:

    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros_disponibles(self):
        for libro in self.libros:
            if libro.disponibilidad:
                print(libro.titulo)

    def enviar_datos_a_base_de_datos(self):
        # Conectamos a la base de datos
        connection = mysql.connector.connect(
            host="localhost", user="root", password="", database="biblioteca"
        )
        cursor = connection.cursor()

        # Insertamos cada libro en la base de datos
        for libro in self.libros:
            cursor.execute("INSERT INTO libros (titulo, autor, isbn, disponibilidad) VALUES (%s, %s, %s, %s)",
                           (libro.titulo, libro.autor, libro.isbn, libro.disponibilidad))

        # Guardamos los cambios en la base de datos
        connection.commit()

        # Cerramos la conexión con la base de datos
        connection.close()


# Creamos un libro
libro = Libro("El Quijote", "Miguel de Cervantes", "978-84-239-0264-7")

# Agregamos el libro a la biblioteca
biblioteca = Biblioteca()
biblioteca.agregar_libro(libro)

# Imprimimos los libros disponibles
biblioteca.mostrar_libros_disponibles()

# Enviamos los datos a la base de datos
biblioteca.enviar_datos_a_base_de_datos()
