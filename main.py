from servicios.sistema import SistemaEstudiantes

sistema = SistemaEstudiantes()

while True:

    print("\n====================================")
    print(" SISTEMA DE GESTIÓN ESTUDIANTIL")
    print("====================================")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante por código")
    print("4. Editar estudiante")
    print("5. Eliminar estudiante")
    print("6. Cantidad de estudiantes")
    print("7. Buscar estudiante por nombre")
    print("8. Ordenar estudiantes")
    print("9. Estadísticas")
    print("10. Información del sistema")
    print("11. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        sistema.agregar_estudiante()

    elif opcion == "2":
        sistema.mostrar_estudiantes()

    elif opcion == "3":
        sistema.buscar_estudiante()

    elif opcion == "4":
        sistema.editar_estudiante()

    elif opcion == "5":
        sistema.eliminar_estudiante()

    elif opcion == "6":
        sistema.cantidad_estudiantes()

    elif opcion == "7":
        sistema.buscar_por_nombre()

    elif opcion == "8":
        sistema.ordenar_estudiantes()

    elif opcion == "9":
        sistema.estadisticas()

    elif opcion == "10":
        sistema.informacion_sistema()

    elif opcion == "11":
        print("\nPrograma finalizado.")
        break

    else:
        print("\n❌ Opción inválida. Intente nuevamente.")
