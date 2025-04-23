from src.Cola import Cola
from src.Pila import Pila

def probar_Pila():
    print("Prueba pila")
    pila = Pila()
    pila.push(1)
    pila.push(2)
    pila.push(3)
    print("Top: ", pila.top())
    print("Size: ", pila.size())
    print("Pop: ", pila.pop())
    print("Reverse: ", pila.reverse().elementos)


probar_Pila()

def probar_Cola():
    print("Prueba Cola")
    cola = Cola()
    cola.push(1)
    cola.push(2)
    cola.push(3)
    print("Top: ", cola.top())
    print("Size: ", cola.size())
    print("Pop: ", cola.pop())
    print("Reverse: ", cola.reverse().elementos)

probar_Cola()