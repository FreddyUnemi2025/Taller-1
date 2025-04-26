from src.metodos.Clases import EmpresaLista, ColaTarea  

def probar_empresa():  
    empresa = EmpresaLista()  

     
    empresa.agregar_tarea(15, ColaTarea("Ventas", "Realizar informe de ventas"))  
    empresa.agregar_tarea(20, ColaTarea("Recursos Humanos", "Actualizar base de datos"))  
    empresa.agregar_tarea(15, ColaTarea("Finanzas", "Preparar presupuesto"))  
    empresa.agregar_tarea(28, ColaTarea("IT", "Actualizar sistema operativo"))  

    # Procesar tareas  
    empresa.procesar_tareas()  

if __name__ == "__main__":  
    probar_empresa()  