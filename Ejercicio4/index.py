from src.metodos.Clases import Tarea, Empleado, EmpresaLista

def probar_empresa():
    empresa = EmpresaLista()

    for i in range(1, 10):
        empresa.agregar_empleado(Empleado())

    for _ in range(200):
        empresa.agregar_tareas(Tarea())
        empresa.asignar_tarea()

    print("\n--- Tareas antes de procesar ---")
    for empleado in empresa.empleados:
        print(f"Empleado {empleado.codigo} tiene {empleado.cantidad_tareas} tareas.")


    print("\n--- Procesando tareas de empleados ---")
    empresa.procesar_tareas()


    print("\n--- Tareas después de procesar ---")
    for empleado in empresa.empleados:
        print(f"Empleado {empleado.nombre} codigo {empleado.codigo} tiene {empleado.cantidad_tareas} tareas.")


if __name__ == "__main__":  
    probar_empresa()