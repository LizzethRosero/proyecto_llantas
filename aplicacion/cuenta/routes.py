import os
from flask import render_template, request, url_for, redirect, flash
import sqlite3
from . import cuenta
from aplicacion.cuenta.forms import Formulariologin, Formularioregistro

@cuenta.route('/login', methods=["GET", "POST"])
def login():
    form = Formulariologin(request.form)

    if form.validate_on_submit():
        username = form.usuariologin.data
        password = form.contraseñalogin.data

        print("Intentando acceder a la base de datos desde la ruta:", os.getcwd())

        conn = sqlite3.connect('aplicacion/database/proyectollantas.db')
        cursor = conn.cursor()

        # Buscar el usuario en la base de datos
        cursor.execute('SELECT * FROM User WHERE nom_usuario = ?', (username,))
        user = cursor.fetchone()

        if user and user[3] == password:  # Comparar la contraseña en texto plano
            # Iniciar sesión (puedes usar Flask-Login para una solución más avanzada)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for("carrito.carrito"))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')

    return render_template('cuentalog.html', form=form)

@cuenta.route('/registro', methods=["GET", "POST"])
def registro():
    form = Formularioregistro(request.form)

    if form.validate_on_submit():
        usuarioreg = form.usuarioreg.data
        email = form.correoreg.data
        password = form.contraseñareg.data

        conn = sqlite3.connect('aplicacion/database/proyectollantas.db')
        cursor = conn.cursor()

        # Verificar si el usuario ya existe
        cursor.execute('SELECT * FROM User WHERE nom_usuario = ? OR correo = ?', (usuarioreg, email))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('Usuario o correo electrónico ya registrados', 'danger')
        else:
            # Insertar la contraseña en texto plano en la base de datos
            cursor.execute('INSERT INTO User (nom_usuario, correo, contraseña) VALUES (?, ?, ?)', (usuarioreg, email, password))
            conn.commit()
            flash('Registro exitoso. ¡Ahora puedes iniciar sesión!', 'success')
            return redirect(url_for("cuenta.login"))

    return render_template('registro.html', form=form)
