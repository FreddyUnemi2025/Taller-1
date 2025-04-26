from metodos.Clases import Cliente, Banco 
class TestBanco:  
    @classmethod  
    def main(cls):  
        banco = Banco()  

        # lo mismo de lo otro de agregar 
        for i in range(1, 6):  
            cliente = Cliente(f'Cliente {i}')  
            banco.agregarCliente(cliente)  

        # lo mismo de antender
        banco.atenderClientes()  

 
if __name__ == "__main__":  
    TestBanco.main()  