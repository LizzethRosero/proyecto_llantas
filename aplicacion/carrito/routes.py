from flask import render_template
from . import carrito
from aplicacion.database.consultasproductos import obtenerproductos

@carrito.route('/carrito')
def carrito():
   productos=obtenerproductos()
   print(productos)
   return render_template('carrito.html', productos=productos)
   