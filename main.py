from flask import Flask, render_template, request, redirect
import profesor_repositorio

app = Flask(__name__)

#------------- Listar -------------
@app.route("/")
def listar():
    profesores = profesor_repositorio.listar()
    return render_template("profesor.html", profesores=profesores)

#------------- Registrar -------------
@app.route("/registro", methods=["POST"])
def registro():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    email = request.form["email"]
    password = request.form["password"]
    calificacion = request.form["calificacion"]
    profesor_repositorio.registro(nombre, apellido, email, password, calificacion)
    return redirect("/")

#------------- Modificar -------------
@app.route("/modificar", methods=["POST"])
def modificar():
    id = request.form["id"]
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    email = request.form["email"]
    password = request.form["password"]
    calificacion = request.form["calificacion"]
    profesor_repositorio.modificar(nombre, apellido, email, password, calificacion)
    return redirect("/")

#------------- Eliminar -------------
@app.route("/eliminar", methods=["POST"])
def eliminar():
    profesor_repositorio.eliminar(request.form["id"])
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)