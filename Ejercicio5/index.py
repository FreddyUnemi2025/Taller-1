from src.dominios.dominio import Caja, Cliente,Supermercado

def prueba():
   supermercado1 = Supermercado()

   supermercado1.agregar_caja(Caja(1))
   supermercado1.agregar_caja(Caja(2))
   supermercado1.agregar_caja(Caja(3))
   
   clientes = [Cliente(1, 100), Cliente(2, 200), Cliente(3, 150),Cliente(4, 300), Cliente(5, 120), Cliente(6, 80)]

   for c in clientes:
      supermercado1.agregar_cliente_a_caja(c)

   print(supermercado1)
   supermercado1.procesar_todos_los_clientes()  

   print("Procesando..")
   print(supermercado1)

if __name__ == "__main__":
    prueba()