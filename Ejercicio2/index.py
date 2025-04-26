from src.metodos.Clases import Cliente, Banco   

def probar_banco():  
    print("Prueba de Banco")  
    
    banco = Banco()  
    
    #  Crea y pone a lo clientes en fila 
    clientes = [Cliente(f'Cliente {i}') for i in range(1, 6)]  
    
    for cliente in clientes:  
        banco.agregarCliente(cliente)  
    
    print(f"Total de clientes en la cola: {len(banco.cola)}")  
    
    # se atiende 
    banco.atenderClientes()  

if __name__ == "__main__":  
    probar_banco()  