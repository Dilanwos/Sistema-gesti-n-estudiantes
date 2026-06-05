from modelos.persona import Persona


class Estudiante(Persona):

    def __init__(self, codigo, nombre, edad, curso):

        super().__init__(nombre, edad)

        self.codigo = codigo
        self.curso = curso

    def mostrar_datos(self):

        print("\n--- ESTUDIANTE ---")
        print("Código:", self.codigo)
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Curso:", self.curso)
