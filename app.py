from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

ARCHIVO_JSON = "datos/estudiantes.json"


def cargar_estudiantes():

    if not os.path.exists(ARCHIVO_JSON):
        return []

    try:
        with open(
            ARCHIVO_JSON,
            "r",
            encoding="utf-8"
        ) as archivo:

            return json.load(archivo)

    except json.JSONDecodeError:
        return []


def guardar_estudiantes(estudiantes):

    with open(
        ARCHIVO_JSON,
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            estudiantes,
            archivo,
            indent=4,
            ensure_ascii=False
        )


@app.route("/")
def inicio():

    return render_template("index.html")


@app.route("/estudiantes")
def estudiantes():

    lista_estudiantes = cargar_estudiantes()

    return render_template(
        "estudiantes.html",
        estudiantes=lista_estudiantes
    )


@app.route("/registrar", methods=["GET", "POST"])
def registrar():

    if request.method == "POST":

        estudiantes = cargar_estudiantes()

        codigo = request.form["codigo"]

        for estudiante in estudiantes:

            if estudiante["codigo"] == codigo:
                return "Ese código ya existe."

        nuevo_estudiante = {
            "codigo": codigo,
            "nombre": request.form["nombre"],
            "edad": int(request.form["edad"]),
            "curso": request.form["curso"]
        }

        estudiantes.append(nuevo_estudiante)

        guardar_estudiantes(estudiantes)

        return redirect("/estudiantes")

    return render_template("registrar.html")


@app.route("/buscar", methods=["GET", "POST"])
def buscar():

    resultado = None

    if request.method == "POST":

        codigo = request.form["codigo"]

        estudiantes = cargar_estudiantes()

        for estudiante in estudiantes:

            if estudiante["codigo"] == codigo:

                resultado = estudiante
                break

    return render_template(
        "buscar.html",
        resultado=resultado
    )


@app.route("/editar/<codigo>", methods=["GET", "POST"])
def editar(codigo):

    estudiantes = cargar_estudiantes()

    estudiante = None

    for e in estudiantes:

        if e["codigo"] == codigo:
            estudiante = e
            break

    if estudiante is None:
        return "Estudiante no encontrado"

    if request.method == "POST":

        estudiante["nombre"] = request.form["nombre"]
        estudiante["edad"] = int(request.form["edad"])
        estudiante["curso"] = request.form["curso"]

        guardar_estudiantes(estudiantes)

        return redirect("/estudiantes")

    return render_template(
        "editar.html",
        estudiante=estudiante
    )


@app.route("/eliminar/<codigo>")
def eliminar(codigo):

    estudiantes = cargar_estudiantes()

    estudiantes = [
        estudiante
        for estudiante in estudiantes
        if estudiante["codigo"] != codigo
    ]

    guardar_estudiantes(estudiantes)

    return redirect("/estudiantes")


if __name__ == "__main__":

    app.run(
        debug=True
    )
