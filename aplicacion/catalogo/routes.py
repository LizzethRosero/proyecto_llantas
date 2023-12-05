from flask import render_template, abort
from . import catalogo
from aplicacion.database.consultasproductos import obtenerproductos #se importa la funcion productos que esta en archivo consu productos

@catalogo.route('/catalogo')
def catalogo():
   try:
      #creacion de variable
      productos=obtenerproductos()
      print(productos)
      return render_template('catalogo.html', productos=productos)# se envia el listado de productos q se obtiene d ela consulta al template
   except:
      abort(500)