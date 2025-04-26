class ColaTarea:  
    def __init__(self, area_solicitante: str, descripcion: str):  
        self.area_solicitante = area_solicitante  
        self.descripcion = descripcion  

    def mostrar_tarea(self):  
        return f'Área: {self.area_solicitante}, Descripción: {self.descripcion}'  


class Empleado:  
    def __init__(self, codigo: int):  
        self.codigo = codigo  
        self.cantidad_tareas = 0  
        self.cola_tareas = []  

    def agregar_tarea(self, tarea: ColaTarea):  
        self.cola_tareas.append(tarea)  
        self.cantidad_tareas += 1  

    def procesar_tarea(self):  
        if self.cola_tareas:  
            tarea = self.cola_tareas.pop(0)  
            self.cantidad_tareas -= 1  
            return tarea  
        return None  

class EmpresaLista:  
    def __init__(self):  
        self.empleados = []  

    def agregar_tarea(self, codigo_empleado: int, tarea: ColaTarea):  
        empleado = next((e for e in self.empleados if e.codigo == codigo_empleado), None)  

        if empleado is None:  
            empleado = Empleado(codigo_empleado)  
            self.empleados.append(empleado)  

        empleado.agregar_tarea(tarea)  

    def procesar_tareas(self):  
        for empleado in self.empleados:  
            if 15 <= empleado.codigo <= 30:  
                tarea = empleado.procesar_tarea()  
                if tarea:  
                    print(f'Tarea procesada para empleado {empleado.codigo}: {tarea.mostrar_tarea()}')  