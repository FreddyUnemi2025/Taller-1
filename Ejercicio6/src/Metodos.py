from faker import Faker
import random

class Lugar:
    fake = Faker('es_ES')
    def __init__(self):
        self.codigo_lugar_votacion = self.fake.random_int(min=1000, max=9999) 
        self.direccion = self.fake.street_address() 
        self.localidad = self.fake.city()  


class Votante:
    fake = Faker('es_ES')
    def __init__(self, codigos_lugares):
        self.dni = self.fake.random_int(min=10000000, max=49999999)
        self.nombre = self.fake.name()
        self.codigo_lugar_votacion = random.choice(codigos_lugares)  # elegimos uno de los códigos
        self.mesa = self.fake.random_int(min=1, max=500)



class Provincia:
    fake = Faker('es_ES')

    def __init__(self):
        self.nombre = self.fake.state()
        self.votantes = []

    def agregar_votante(self, votante):
        self.votantes.append(votante)

    

class Fecha: 
    def __init__(self, año, mes, dia):
        self.año = año
        self.mes = mes
        self.dia = dia
        

class PadronElectoral:
    def __init__(self, fecha):
        self.fecha = fecha
        self.lista_provincias = []  
        self.lista_lugares = []    

    def agregar_provincias(self, provincia):
        self.lista_provincias.append(provincia)

    def agregar_lugar_votacion(self, lugar):
        self.lista_lugares.append(lugar)
    
    def Consultar_Lugar_Votacion(self, provincia, dni_votante, lista_lugares):
        if hasattr(provincia, 'votantes'):
            for votante in provincia.votantes:
                if votante.dni == dni_votante:
                    direccion = ''
                    localidad = ''
                    mesa = votante.mesa

                    for lugar in lista_lugares:
                        if lugar.codigo_lugar_votacion == votante.codigo_lugar_votacion:
                            direccion = lugar.direccion
                            localidad = lugar.localidad
                            break

                    registro = {
                        'direccion': direccion,
                        'localidad': localidad,
                        'mesa': mesa
                    }
                    return True, registro

        return False, None
