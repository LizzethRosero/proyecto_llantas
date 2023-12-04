from flask import render_template, request, url_for, redirect
from . import cuenta
from .forms import Formulariologin, Formularioregistro

@cuenta.route('/login', methods=["GET", "POST"])
def login():
   form = Formulariologin(request.form)
   #validacion datos ususrio y contraseña
   if form.validate_on_submit():
      #realizar el proceso de inicop de sesion  o login
      return redirect(url_for("catalogo.catalogo"))
   else:
      return render_template('cuentalog.html', form=form)

@cuenta.route('/login/registro', methods=["GET", "POST"])
def registro():
   form = Formularioregistro(request.form)
   #validacion datos ususrio y contraseña
   if form.validate_on_submit():
      #realizar el proceso de inicop de sesion  o login
      return redirect(url_for("catalogo.catalogo"))
   else:
      return render_template('registro.html', form=form)