from flask import render_template
from . import catalogo


@catalogo.route('/catalogo')
def catalogo():
   return render_template('catalogo.html')