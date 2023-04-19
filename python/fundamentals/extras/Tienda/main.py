from tienda import Tienda
from Producto import Producto

mi_tienda = Tienda("Mi Tienda")

producto_1 = Producto("Polera 1 ", 5.99,  " hombre")
producto_2 = Producto("Polera 2 ", 10.99, " mujer")
producto_3 = Producto("Polera 3 ", 5.99,  " niña")
producto_4 = Producto("Polera 4 ", 10.99, " niño")
producto_5 = Producto("Polera 5 ", 12.99, " hombre")
producto_6 = Producto("Polera 6 ", 5.99, " unisex")

mi_tienda.agregar_producto(producto_1).agregar_producto(producto_2).agregar_producto(producto_3).agregar_producto(producto_4).agregar_producto(producto_5).agregar_producto(producto_6)

mi_tienda.imprimir_productos()