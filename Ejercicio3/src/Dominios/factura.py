class Producto:
    def __init__(self, codigo, precio):
        self.codigo = codigo
        self.precio = precio

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    
    def actualizar_codigo(self, nuevo_codigo):
        self.codigo = nuevo_codigo

    def __str__(self):
        return f"Código: {self.codigo}, Precio: ${self.precio}"


class Factura:
    def __init__(self, numero):
        self.numero = numero
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def consultar_numero(self):
        return self.numero

    def consultar_productos(self):
        return self.productos

    def actualizar_producto(self, indice, nuevo_producto):
        if 0 <= indice < len(self.productos):
            self.productos[indice] = nuevo_producto

    def __str__(self):
        detalle = f"Factura Nº {self.numero}:\n"
        for i, producto in enumerate(self.productos, start=1):
            detalle += f"  {i}. {producto}\n"
        return detalle
    
    
class Tienda:
    def __init__(self):
        self.facturas = []

    def registrar_factura(self, factura):
        self.facturas.append(factura)

    def mostrar_facturas(self):
        for factura in self.facturas:
            print(factura)

