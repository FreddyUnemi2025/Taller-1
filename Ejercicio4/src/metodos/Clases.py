from faker import Faker

fake = Faker('es_ES')

class Tarea:
    def __init__(self, area_solicitante=None, descripcion=None):
        self.area_solicitante = area_solicitante if area_solicitante else fake.job()
        self.descripcion = descripcion if descripcion else fake.sentence()

    def mostrar_tarea(self):
        return f"Área: {self.area_solicitante} | Descripción: {self.descripcion}"

class Empleado:
    contador_codigo = 1 
    
    def __init__(self, nombre=None, genero=None):
        self.codigo = Empleado.contador_codigo
        Empleado.contador_codigo += 1 
        
        self.nombre = nombre if nombre else fake.name()
        self.genero = genero if genero else fake.random_element(elements=('Masculino', 'Femenino'))
        self.cantidad_tareas = 0
        self.cola_tareas = []

    def agregar_tarea(self, tarea):
        self.cola_tareas.append(tarea)
        self.cantidad_tareas += 1

    

class EmpresaLista:
    def __init__(self):
        self.empleados = []
        self.tareas = []

    def agregar_empleado(self, empleado):
        for e in self.empleados:
            if e.codigo == empleado.codigo: 
                return "No se puede agregar un empleado con el mismo código"
        
        self.empleados.append(empleado)
        return "Empleado agregado"

    def agregar_tareas(self, Tarea):
        self.tareas.append(Tarea)

    def asignar_tarea(self):
        if not self.empleados:
            print("No hay empleados para asignar tareas.")
            return

        empleado_con_menos_tareas = min(self.empleados, key=lambda e: e.cantidad_tareas)
        empleado_con_menos_tareas.agregar_tarea(self.tareas.pop(0))

    def procesar_tareas(self):
        for empleado in self.empleados:
            if 15 <= empleado.codigo <= 30:
                while empleado.cola_tareas:
                    tarea = empleado.cola_tareas.pop(0)
                    empleado.cantidad_tareas -= 1
                    print(f"Procesada tarea para Empleado {empleado.nombre}({empleado.codigo}): {tarea.mostrar_tarea()}")


lista = [1,2,3,4,5]
a = lista.pop(0)
a = 1
lista = [2,3,4,5]