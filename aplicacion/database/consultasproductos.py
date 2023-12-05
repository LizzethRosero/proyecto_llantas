# se define funciones para hacer consultas en la BD en la tabla proudctos
import sqlite3
from flask import current_app

def obtenerproductos ():
    ruta=current_app.config['DATABASE_URI'].replace('sqlite:///','') # encontrol la url de la bd,replace quita sqlite(en que carpet se encutra la bd)
    conexion=sqlite3.connect(ruta)

    cursor=conexion.cursor()#para relizar consultas mediante un cursor
    cursor.execute("""SELECT Productos.id, Marca.marca, Productos.medida, Productos.costo, Productos.descripcion, Productos.imagen
        FROM Productos
        INNER JOIN Marca ON Productos.marca = Marca.id;
        """) 
    productos=cursor.fetchall()#fetcholl varios productos-guardar productos de la consulta
    conexion.close()

    #retornar productos
    return productos
