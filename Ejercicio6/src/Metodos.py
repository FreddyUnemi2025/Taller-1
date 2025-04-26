
class Lugar:
    def __init__(self, codigo_lugar_votacion, direccion, localidad):
        self.codigo_lugar_votacion = codigo_lugar_votacion
        self.direccion = direccion
        self.localidad = localidad


class Votante:
    def __init__(self, dni, nombre, codigo_lugar, mesa):
        self.dni = dni
        self.nombre = nombre
        self.codigo_lugar_votacion = codigo_lugar
        self.mesa = mesa


class Provincia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.votantes = []

    def agregar_votante(self, votante):
        self.votantes.append(votante)

    

class Fecha: 
    def __init__(self, año, mes, dia):
        self.año = año
        self.mes = mes
        self.dia = dia
        

class PadronElectoral:
    def __init__(self, fecha_actualizacion):
        self.fecha_actualizacion = fecha_actualizacion
        self.lista_provincias = []  
        self.lista_lugares = []    

    def agregar_provincias(self, provincia):
        self.lista_provincias.append(provincia)

    def agregar_lugar_votacion(self, lugar):
        self.lista_lugares.append(lugar)
