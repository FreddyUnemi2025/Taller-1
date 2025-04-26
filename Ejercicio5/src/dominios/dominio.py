from src.Tad.cola import Cola
class Cliente:
    def __init__(self, num, monto):
        self.num = num
        self.monto = monto

    def __str__(self):
        return f"Cliente {self.num} - Monto: ${self.monto}"

class Caja:
    def __init__(self, numero):
        self.numero = numero
        self.recaudacion = 0.0
        self.clientes_atendidos = 0
        self.cola_clientes = Cola()

    def agregar_cliente(self, cliente):
        self.cola_clientes.encolar(cliente)

    def procesar_clientes(self):
        while not self.cola_clientes.is_empty():
            cliente = self.cola_clientes.desencolar()
            self.recaudacion += cliente.monto
            self.clientes_atendidos += 1

    def cantidad_por_atender(self):
        return len(self.cola_clientes)

    def __str__(self):
        return (f"Caja {self.numero}  Recaudación: ${self.recaudacion} Atendidos: {self.clientes_atendidos}  En espera: {self.cantidad_por_atender()}")
    
class Supermercado:
    def __init__(self):
        self._lista_cajas = []  

    def agregar_caja(self, caja):
        self._lista_cajas.append(caja)

    def procesar_todos_los_clientes(self):
        for caja in self._lista_cajas:
            caja.procesar_clientes()

    def agregar_cliente_a_caja(self, cliente):
        if not self._lista_cajas:
            print("No hay cajas disponibles.")
            return
        caja_mas_libre = min(self._lista_cajas, key=lambda c: c.cantidad_por_atender())
        caja_mas_libre.agregar_cliente(cliente)

    def __str__(self):
        info = "Estado del supermercado:\n"
        for caja in self._lista_cajas:
            info += str(caja) + "\n"
        return info

