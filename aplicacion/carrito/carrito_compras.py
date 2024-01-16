class Producto_Carrito:
    def __init__(self,id_producto,cantidad,precio):
        self.id_producto=id_producto
        self.cantidad=cantidad
        self.precio=precio

class Carrito:
    def __init__(self):
        #self.id_usuario=id_usuario
        self.cantidad_productos=0
        self.valor_total=0
        self.productos=[]

    def agregar_producto (self,producto: Producto_Carrito):
        for item in self.productos:
            if item.id_producto==producto.id_producto:
                item.cantidad+=producto.cantidad
                item.precio+=producto.precio
                self.cantidad_productos+=producto.cantidad
                self.valor_total+=producto.precio
            return
        self.productos.append(producto)    
        self.cantidad_productos+=producto.cantidad
        self.valor_total+=producto.precio
carrito_compras=Carrito()        



