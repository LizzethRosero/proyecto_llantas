from flask import render_template
from . import cuenta


@cuenta.route('/login')
def login():
   return render_template('cuentalog.html')

@cuenta.route('/login/registro')
def registro():
   return render_template('registro.html')