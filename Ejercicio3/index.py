from src.Dominios.factura import Factura, Producto,Tienda

def prueba():
    factura = Factura("F01")
    
    factura.agregar_producto(Producto("C1", 24))
    factura.agregar_producto(Producto("H23", 234))
    factura.agregar_producto(Producto("M30", 109))
    
    print("Factura original:")
    print(factura)
    
    factura.actualizar_producto(1, Producto("K123", 247))
    
    print("Factura actualizada:")
    print(factura)
    
    print("Registro de la Tienda")
    tienda = Tienda()
    tienda.registrar_factura(factura)
    tienda.mostrar_facturas()

if __name__ == "__main__":
    prueba()
