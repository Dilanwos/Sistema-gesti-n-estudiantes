# Sistema de Gestión Estudiantil

Proyecto desarrollado en Python aplicando los principios de la Programación Orientada a Objetos (POO).

## Descripción

Este sistema permite administrar estudiantes mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar), implementando conceptos fundamentales de POO como clases, objetos y herencia.

La información se almacena de forma persistente utilizando archivos JSON, permitiendo conservar los datos incluso después de cerrar el programa.

---

## Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos (POO)
- JSON para persistencia de datos
- Git y GitHub para control de versiones

---

## Estructura del proyecto

```text
SistemaEstudiantes/
│
├── main.py
│
├── modelos/
│   ├── persona.py
│   └── estudiante.py
│
├── servicios/
│   └── sistema.py
│
├── datos/
│   └── estudiantes.json
│
├── .gitignore
│
└── README.md
```

---

## Funcionalidades

### Gestión de estudiantes

- Registrar estudiantes
- Mostrar estudiantes
- Buscar estudiantes por código
- Editar estudiantes
- Eliminar estudiantes

### Funciones adicionales

- Contar estudiantes registrados
- Buscar estudiantes por nombre
- Ordenar estudiantes por:
  - Nombre
  - Edad
  - Código

### Estadísticas

- Cantidad total de estudiantes
- Promedio de edad
- Edad mayor
- Edad menor

### Persistencia

- Guardado automático en JSON
- Carga automática de estudiantes al iniciar el sistema

### Validaciones

- Validación de edad
- Validación de nombres vacíos
- Validación de cursos vacíos
- Validación de códigos duplicados

---

## Conceptos de POO aplicados

### Clase Persona

Contiene los atributos comunes:

- Nombre
- Edad

### Clase Estudiante

Hereda de Persona y agrega:

- Código
- Curso

### Herencia

```text
Persona
   ↑
Estudiante
```

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

2. Ingresar a la carpeta

```bash
cd SistemaEstudiantes
```

3. Ejecutar el programa

```bash
python main.py
```

---

## Autor

Dilan Chirva

---

## Versión

Versión 1.0
