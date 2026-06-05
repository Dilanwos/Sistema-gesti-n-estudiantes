from modelos.estudiante import Estudiante


class SistemaEstudiantes:

    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self):

        codigo = input("Código: ")

        for estudiante in self.estudiantes:
            if estudiante.codigo == codigo:
                print("Ese código ya existe.")
                return

        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        curso = input("Curso: ")

        nuevo = Estudiante(
            codigo,
            nombre,
            edad,
            curso
        )

        self.estudiantes.append(nuevo)

        print("Estudiante registrado.")

    def mostrar_estudiantes(self):

        if len(self.estudiantes) == 0:
            print("No hay estudiantes registrados.")
            return

        for estudiante in self.estudiantes:
            estudiante.mostrar_datos()

    def buscar_estudiante(self):

        codigo = input("Ingrese código: ")

        for estudiante in self.estudiantes:
            if estudiante.codigo == codigo:
                estudiante.mostrar_datos()
                return

        print("No encontrado.")

    def editar_estudiante(self):

        codigo = input("Código a editar: ")

        for estudiante in self.estudiantes:

            if estudiante.codigo == codigo:

                estudiante.nombre = input("Nuevo nombre: ")
                estudiante.edad = int(input("Nueva edad: "))
                estudiante.curso = input("Nuevo curso: ")

                print("Actualizado correctamente.")
                return

        print("Estudiante no encontrado.")

    def eliminar_estudiante(self):

        codigo = input("Código a eliminar: ")

        for estudiante in self.estudiantes:

            if estudiante.codigo == codigo:

                self.estudiantes.remove(estudiante)

                print("Estudiante eliminado.")
                return

        print("Estudiante no encontrado.")

    def cantidad_estudiantes(self):

        print(
            f"\nTotal de estudiantes registrados: {len(self.estudiantes)}"
        )

    def buscar_por_nombre(self):

        nombre = input("Ingrese el nombre: ")

        encontrado = False

        for estudiante in self.estudiantes:

            if estudiante.nombre.lower() == nombre.lower():

                estudiante.mostrar_datos()
                encontrado = True

        if not encontrado:
            print("No se encontró ningún estudiante.")

    def ordenar_estudiantes(self):

        print("\n=== ORDENAR ESTUDIANTES ===")
        print("1. Ordenar por nombre")
        print("2. Ordenar por edad")
        print("3. Ordenar por código")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            self.estudiantes.sort(
                key=lambda estudiante: estudiante.nombre.lower()
            )

            print("Estudiantes ordenados por nombre.")

        elif opcion == "2":

            self.estudiantes.sort(
                key=lambda estudiante: estudiante.edad
            )

            print("Estudiantes ordenados por edad.")

        elif opcion == "3":

            self.estudiantes.sort(
                key=lambda estudiante: estudiante.codigo
            )

            print("Estudiantes ordenados por código.")

        else:
            print("Opción inválida.")
