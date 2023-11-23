class Libro:

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponibilidad = True

    def prestar(self):
        self.disponibilidad = False

    def __str__(self) -> str:
        return f'{"Titulo: %s" % self.titulo}\n' f'{"Autor: %s" % self.autor}\n' f'{"Isbn: %s" % self.isbn}\n' f'{"Disponibilidad: %s" % "Sí" if self.disponibilidad == True else "Disponibilidad: %s" % "No"}'


libro1 = Libro("Los caballeros del más allá", "Pedro Escamoso", 91991352)
libro1.prestar()
print(libro1)
