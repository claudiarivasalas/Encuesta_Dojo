from flask import Flask, render_template, request, redirect, session
from encuesta_dojo_app import app

@app.route('/')
def formulario():
    return render_template('encuesta.html')

@app.route('/process', methods=["POST"])
def ingreso_datos():
    print(request.form)
    session['nombre'] = request.form['name']
    session['ciudad'] = request.form['city']
    session['lenguaje'] = request.form['language']
    session['comentarios'] = request.form['comments']
    return redirect('/result')


@app.route('/result')
def muestra_datos():
    print(request.form)
    return render_template('show.html')