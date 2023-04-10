class Tienda:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        producto.tienda = self

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.tienda = None

mi_tienda = Tienda("Mi Tienda", "123 Calle Principal")

producto_1 = Producto("Producto 1", 10.99)

mi_tienda.agregar_producto(producto_1)
print(mi_tienda.nombre)
print(mi_tienda.productos[0].nombre)