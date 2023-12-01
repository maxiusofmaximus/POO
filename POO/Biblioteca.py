import mysql.connector
from tabulate import tabulate


class BaseDeDatos:

    def __init__(self, host, usuario, contrasenna, database):
        self.conexion = mysql.connector.connect(
            host=host, user=usuario, password=contrasenna, database=database
        )
        self.cursor = self.conexion.cursor()

    def ejecutar_consulta(self, consulta):
        self.cursor.execute(consulta)
        self.connection.commit()

    def obtener_resultados(self, consulta):
        self.cursor.execute(consulta)
        return self.cursor.fetchall()

class Usuario:
    def __init__(self):
        self.cedula = None
        self.nombre = None
        self.apellido = None
        self.fecha_nacimiento = None
        self.nacionalidad = None
        self.correo = None
        self.telefono = None


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
        consulta = f"INSERT INTO libros (titulo, autor, isbn, disponibilidad) VALUES {(self.libros[0].titulo, self.libros[0].autor, self.libros[0].isbn, self.libros[0].disponibilidad)}"
        self.base_de_datos.ejecutar_consulta(consulta)

    def obtener_libros_disponibles(self):
        """
        Obtiene los libros disponibles de la base de datos.
    
        Returns:
            Una lista con los libros disponibles.
        """

        consulta = "SELECT * FROM libros WHERE disponibilidad = 1"
        datos = self.base_de_datos.obtener_resultados(consulta)
        return datos

    def mostrar_libros_disponibles(self):
        """
        Muestra los libros disponibles.
    
        Args:
            libros: La lista con los libros disponibles.
        """

        libros = self.obtener_libros_disponibles()
        print(tabulate(libros, headers=[
            "ID", "TITULO", "AUTOR", "ISBN", "DISPONIBILIDAD"], tablefmt="pipe"))


    def prestar_libros(self):
        consulta = "SELECT * FROM libros WHERE disponibilidad = 1"
        datos = self.base_de_datos.obtener_resultados(consulta)
        id_libro = int(input(
            "Ingrese el id del libro que desea prestar: "))
        for libro_en_biblioteca in datos:
            if libro_en_biblioteca[0] == id_libro:
                consulta = f"UPDATE libros SET disponibilidad = 0 WHERE id = '{id_libro}'"
                base_de_datos.ejecutar_consulta(consulta)

    def devolver_libros(self):
        consulta = "SELECT * FROM libros WHERE disponibilidad = 0"
        datos = self.base_de_datos.obtener_resultados(consulta)
        id_libro = int(input(
            "Ingrese el id del libro que desea devolver: "))
        for libro_en_biblioteca in datos:
            if libro_en_biblioteca[0] == id_libro:
                consulta = f"UPDATE libros SET disponibilidad = 1 WHERE id = '{id_libro}'"
                base_de_datos.ejecutar_consulta(consulta)

    def crear_usuario(self):
        usuario = Usuario()
        usuario.cedula = input("Ingrese su cédula: ")
        usuario.nombre = input("Ingrese su nombre: ")
        usuario.apellido = input("Ingrese su apellido: ")
        usuario.fecha_nacimiento = input("Ingrese su fecha de nacimiento: ")
        usuario.nacionalidad = input("Ingrese su nacionalidad: ")
        usuario.correo = input("Ingrese su correo: ")
        usuario.telefono = input("Ingrese su telefono: ")

    def validar_usuario(self):
        cedula = input("Ingrese su cedula: ")
        print("Validando usuario entre la base de datos, por favor espere...")
        consulta = f"SELECT * FROM usuarios"
        datos = self.base_de_datos.obtener_resultados(consulta)
        print(tabulate(datos, headers=[
              "ID", "CEDULA", "NOMBRE", "APELLIDO", "FECHA_NACIMIENTO", "NACIONALIDAD", "CORREO", "TELEFONO"], tablefmt="pipe"))
        for dato in datos:
            id, ced, nombre, apellido, fecha_nacimiento, nacionalidad, correo, telefono = dato
        if(cedula == ced):
            print("El usuario es válido para prestar libros")
            self.prestar_libros()
        else:
            print("El usuario no es válido para prestar libros, primero debe de crear un usuario")
            self.crear_usuario()
    

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
                consulta = f"DELETE FROM libros WHERE id = {id_libro}"
                base_de_datos.ejecutar_consulta(consulta)

            case "3":
                biblioteca.mostrar_libros_disponibles()

            case "4":
                biblioteca.validar_usuario()

            case "5":
                biblioteca.devolver_libros()

            case "6":
                print("Has salido del menú de opciones")
                break
            case _:
                print("Opción incorrectamente seleccionada")
