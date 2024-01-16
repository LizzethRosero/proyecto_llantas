import os
from flask import render_template, request, url_for, redirect, flash, session
import sqlite3
from . import cuenta
from aplicacion.cuenta.forms import Formulariologin, Formularioregistro
from aplicacion.database.consultasusuarios import consultar_usuario

@cuenta.route('/login', methods=["GET", "POST"])
def login():
    if "username" in session:
        return  redirect(url_for("inicio.inicio"))
    
    form = Formulariologin(request.form)

    if form.validate_on_submit():
        username = form.usuariologin.data
        password = form.contraseñalogin.data

        usuario_existe=consultar_usuario(username)
        print(f"Intentando acceder a la base de datos  con usuario: {usuario_existe} ")

        if usuario_existe:
            print("Usuario existe")
            if usuario_existe[3] == password:
                flash('Inicio de sesión exitoso', 'success')
                session["username"]=username
                return redirect(url_for("carrito.carrito"))
            else:
                #contraseña incorrecta 
                flash("La contraseña no es correcta", "danger")
        else:
            flash('Usuario no esta registrado', 'danger')

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

@cuenta.route('/cerrar_sesion')
def cerrar_sesion():
    if "username" in session:
        session.pop("username",None)
    return redirect(url_for("cuenta.login"))   

