from flask import render_template, session, redirect, url_for,request, flash
from . import carrito
from aplicacion.database.consultasproductos import obtenerproductos,obtenerproducto
from aplicacion.carrito.carrito_compras import carrito_compras, Producto_Carrito

@carrito.route('/carrito')
def carrito():
   if "username" not in session:
      return  redirect(url_for("cuenta.login"))
   
   productos=obtenerproductos()
   print(productos)
   return render_template('carrito.html', productos=productos)

@carrito.route('/agregar_producto/<id_producto>', methods=["GET", "POST"])
def agregar_producto(id_producto):
   if "username" not in session:
      return redirect(url_for("cuenta.login"))
   if request.method=="POST":
      cantidad = int(request.form['cantidad'])
      print(f"cantidad: {cantidad}")
      if cantidad>0:
         producto=obtenerproducto(id_producto)
         precio_producto=producto[3]
         precio_x_cantidad=cantidad*precio_producto

         producto_carrito=Producto_Carrito(id_producto, cantidad,precio_x_cantidad)
         carrito_compras.agregar_producto(producto_carrito)
         flash("Producto Agregado","success")
         return redirect(url_for("carrito.carrito"))
      else:
         flash("Error la cantidad no puede ser menor o igual a 0", "danger")
         return redirect(url_for("carrito.carrito"))
   return redirect(url_for("carrito.carrito"))


   