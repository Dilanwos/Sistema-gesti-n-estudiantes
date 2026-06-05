import json
import os

from modelos.estudiante import Estudiante


class SistemaEstudiantes:

    def __init__(self):

        self.estudiantes = []

        self.cargar_estudiantes()

    def agregar_estudiante(self):

        codigo = input("Código: ").strip()

        for estudiante in self.estudiantes:
            if estudiante.codigo == codigo:
                print("Ese código ya existe.")
                return

        nombre = input("Nombre: ").strip()

        if not nombre:
            print("El nombre no puede estar vacío.")
            return

        while True:

            try:
                edad = int(input("Edad: "))

                if edad <= 0:
                    print("La edad debe ser mayor que 0.")
                    continue

                break

            except ValueError:
                print("Ingrese una edad válida.")

        curso = input("Curso: ").strip()

        if not curso:
            print("El curso no puede estar vacío.")
            return

        nuevo = Estudiante(
            codigo,
            nombre,
            edad,
            curso
        )

        self.estudiantes.append(nuevo)

        self.guardar_estudiantes()

        print("Estudiante registrado correctamente.")

    def mostrar_estudiantes(self):

        if len(self.estudiantes) == 0:
            print("No hay estudiantes registrados.")
            return

        print("\n=== LISTA DE ESTUDIANTES ===")

        for estudiante in self.estudiantes:
            estudiante.mostrar_datos()

    def buscar_estudiante(self):

        codigo = input("Ingrese código: ").strip()

        for estudiante in self.estudiantes:

            if estudiante.codigo == codigo:
                estudiante.mostrar_datos()
                return

        print("Estudiante no encontrado.")

    def editar_estudiante(self):

        codigo = input("Código a editar: ").strip()

        for estudiante in self.estudiantes:

            if estudiante.codigo == codigo:

                nuevo_nombre = input("Nuevo nombre: ").strip()

                if nuevo_nombre:
                    estudiante.nombre = nuevo_nombre

                while True:

                    try:
                        nueva_edad = int(input("Nueva edad: "))

                        if nueva_edad <= 0:
                            print("La edad debe ser mayor que 0.")
                            continue

                        estudiante.edad = nueva_edad
                        break

                    except ValueError:
                        print("Ingrese una edad válida.")

                nuevo_curso = input("Nuevo curso: ").strip()

                if nuevo_curso:
                    estudiante.curso = nuevo_curso

                self.guardar_estudiantes()

                print("Estudiante actualizado correctamente.")
                return

        print("Estudiante no encontrado.")

    def eliminar_estudiante(self):

        codigo = input("Código a eliminar: ").strip()

        for estudiante in self.estudiantes:

            if estudiante.codigo == codigo:

                self.estudiantes.remove(estudiante)

                self.guardar_estudiantes()

                print("Estudiante eliminado correctamente.")
                return

        print("Estudiante no encontrado.")

    def cantidad_estudiantes(self):

        print(
            f"\nTotal de estudiantes registrados: {len(self.estudiantes)}"
        )

    def buscar_por_nombre(self):

        nombre = input("Ingrese el nombre: ").strip()

        encontrado = False

        for estudiante in self.estudiantes:

            if estudiante.nombre.lower() == nombre.lower():

                estudiante.mostrar_datos()
                encontrado = True

        if not encontrado:
            print("No se encontró ningún estudiante.")

    def ordenar_estudiantes(self):

        if len(self.estudiantes) == 0:
            print("No hay estudiantes registrados.")
            return

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

    def estadisticas(self):

        if len(self.estudiantes) == 0:
            print("No hay estudiantes registrados.")
            return

        edades = [
            estudiante.edad
            for estudiante in self.estudiantes
        ]

        promedio = sum(edades) / len(edades)

        print("\n=== ESTADÍSTICAS ===")
        print(
            f"Cantidad de estudiantes: {len(self.estudiantes)}"
        )
        print(
            f"Promedio de edad: {promedio:.2f}"
        )
        print(
            f"Edad mayor: {max(edades)}"
        )
        print(
            f"Edad menor: {min(edades)}"
        )

    def informacion_sistema(self):

        print("\n=== INFORMACIÓN DEL SISTEMA ===")
        print("Proyecto: Sistema de Gestión Estudiantil")
        print("Versión: 2.0")
        print("Autor: Dilanwos")
        print("Paradigma: Programación Orientada a Objetos")

    def guardar_estudiantes(self):

        datos = []

        for estudiante in self.estudiantes:

            datos.append({
                "codigo": estudiante.codigo,
                "nombre": estudiante.nombre,
                "edad": estudiante.edad,
                "curso": estudiante.curso
            })

        os.makedirs("datos", exist_ok=True)

        with open(
            "datos/estudiantes.json",
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

    def cargar_estudiantes(self):

        ruta = "datos/estudiantes.json"

        if not os.path.exists(ruta):
            return

        try:

            with open(
                ruta,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

                for estudiante in datos:

                    nuevo = Estudiante(
                        estudiante["codigo"],
                        estudiante["nombre"],
                        estudiante["edad"],
                        estudiante["curso"]
                    )

                    self.estudiantes.append(nuevo)

        except json.JSONDecodeError:
            print("Error al leer estudiantes.json")
