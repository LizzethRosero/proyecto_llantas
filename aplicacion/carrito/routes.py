from flask import render_template, session, redirect, url_for,request, flash
from . import carrito
from aplicacion.database.consultasproductos import obtenerproductos,obtenerproducto
from aplicacion.carrito.carrito_compras import carrito_compras, Producto_Carrito

@carrito.route('/productos')
def productos():
   if "username" not in session:
      return redirect(url_for("cuenta.login"))
   
   productos=obtenerproductos()
   # print(productos)
   return render_template('carrito.html', productos=productos)

@carrito.route('/agregar_producto/<id_producto>', methods=["GET", "POST"])
def agregar_producto(id_producto):
   if "username" not in session:
      return redirect(url_for("cuenta.login"))
   if request.method=="POST":
      producto=obtenerproducto(id_producto)
      print(f"Producto id: {producto[0]}")
      precio_producto=producto[3]
      try:
         cantidad = int(request.form.get(f'cantidad_{id_producto}'))
         print(f"cantidad: {cantidad}")
         if cantidad>0:
            
            precio_x_cantidad=cantidad*precio_producto

            producto_carrito=Producto_Carrito(id_producto, cantidad,precio_x_cantidad)
            carrito_compras.agregar_producto(producto_carrito)
            flash("Producto Agregado","success")
            return redirect(url_for("carrito.productos"))
         else:
            flash("Error la cantidad no puede ser menor o igual a 0", "danger")
            return redirect(url_for("carrito.productos"))
      except Exception as e:
         flash(f"Error de cantidad: Debe ser un número mayor a cero","danger")
   return redirect(url_for("carrito.productos"))

