
# 7) Crear un producto mínimo viable (Mínima Funcionalidad del Software) a partir del modelo UML.

class Cliente():
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion


class Item():
    def __init__(self, peso, descripcion):
        self.peso = peso
        self.descripcion = descripcion

    def precioPorCantidad(self):
        return int(input(f"Precio por unidad de '{self.descripcion}': "))

    def ObtenerPeso(self):
        self.peso = int(input(f"Peso en kg de '{self.descripcion}': "))
        return self.peso


class DetalleOrden():
    def __init__(self, cantidad, tipoImpuesto):
        self.cantidad = cantidad
        self.tipoImpuesto = tipoImpuesto

    def CalclSubtotal(self, item):
        return self.cantidad * item.precioPorCantidad()

    def CalcPeso(self, item):
        return self.cantidad * item.ObtenerPeso()


class Orden():
    def __init__(self, fecha, estado):
        self.fecha = fecha
        self.estado = estado

    def CalcImpuesto(self, detalles, item):
        subtotal = detalles.CalclSubtotal(item)
        tipo = detalles.tipoImpuesto

        if tipo == "IVA":
            impuesto = subtotal * 0.12
        elif tipo == "IBI":
            impuesto = subtotal * 0.10
        elif tipo == "PATRIMONIO":
            impuesto = subtotal * 0.08
        else:
            impuesto = 0
        
        return subtotal, impuesto

    def CalcTotal(self, detalles, item):
        subtotal, impuesto = self.CalcImpuesto(detalles, item)
        return subtotal + impuesto

    def CalcPesoTotal(self, detalles, item):
        return detalles.CalcPeso(item)

class Pago:
    def __init__(self, monto):
        self.monto = monto

class Credito(Pago):
    def __init__(self, monto, fecha, numero, tipo):
        super().__init__(monto)
        self.fecha = fecha
        self.numero = numero
        self.tipo = tipo

class Efectivo(Pago):
    def __init__(self, monto, moneda):
        super().__init__(monto)
        self.moneda = moneda

class Cheque(Pago):
    def __init__(self, monto, nombre, identifBanco):
        super().__init__(monto)
        self.nombre = nombre
        self.identifBanco = identifBanco
