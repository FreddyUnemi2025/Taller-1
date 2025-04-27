from src.Metodos import Cliente, Orden, DetalleOrden, Item, Pago, Credito, Efectivo, Cheque
import datetime

def prueba():
    cliente1 = Cliente("Freddy", "Av. Principal 123")

    item1 = Item(2, "Laptop")
    
    detalle = DetalleOrden(cantidad=2, tipoImpuesto="IVA")

    orden1 = Orden("2025-04-12", "En proceso")

    total = orden1.CalcTotal(detalle, item1)
    peso = orden1.CalcPesoTotal(detalle, item1)
    
    si = 'si'
    moneda = 'Dolar'
    while si == 'si':
        tipo_pago = str(input("Elige el tipo de pago (Efectivo, Credito, Cheque): "))
        if tipo_pago == 'Efectivo':
            moneda = input("Elige la divisa (Euro/Dolar):")
            mi_pago = Efectivo(total, moneda)
            break
        elif tipo_pago == 'Credito':
            fecha = datetime.datetime.now()
            tipo = input("Elige tipo de credito (Minimo/Diferido):")
            numero = input("Numero de tarjeta: ")
            mi_pago = Credito(total, fecha, numero, tipo)
            break
        elif tipo_pago == 'Cheque':
            identificacion = input("Su identificacion del banco: ")
            mi_pago = Cheque(total, cliente1.nombre, identificacion)
            break

        print("Porfavor escriba correctamente una de las opciones...\n")
            
    print("\n---ORDEN ---")
    print("Cliente:", cliente1.nombre)
    print("Dirección:", cliente1.direccion)
    print("Descripción del Item:", item1.descripcion)
    print("Cantidad:", detalle.cantidad)
    print("Total a pagar:", total, moneda)
    print("Peso total del pedido:", peso, "kg")
    print("Tipo de pago:", tipo_pago)

if __name__ == "__main__":
    prueba()