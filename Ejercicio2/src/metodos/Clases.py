from typing import List
class Cliente:  
    def __init__(self, nombre: str):  
        self.nombre = nombre  

    def serAtendido(self):  
        print(f'La persona {self.nombre} ha sido atendida.')  

class Cajero:  
    def __init__(self, nombre: str):  
        self.nombre = nombre  

    def atender(self, cliente: Cliente):  
        cliente.serAtendido()  

class Banco:  
    def __init__(self):  
        self.cola: List[Cliente] = []  
        self.cajero = Cajero("Cajero 1")  
        
    def agregarCliente(self, cliente: Cliente):  
        self.cola.append(cliente)  

    def atenderClientes(self):  
        while self.cola:  
            cliente = self.cola.pop(0)  
            self.cajero.atender(cliente)  
