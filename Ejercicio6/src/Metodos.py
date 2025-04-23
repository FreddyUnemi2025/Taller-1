
class LugarVotacion:
    def __init__(self, codigo, direccion, localidad):
        self.codigo = codigo
        self.direccion = direccion
        self.localidad = localidad


class Votante:
    def __init__(self, dni, nombre, codigo_lugar, mesa):
        self.dni = dni
        self.nombre = nombre
        self.codigo_lugar = codigo_lugar
        self.mesa = mesa


class Provincia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.votantes = []  


class Padron2025:
    def __init__(self, fecha_actualizacion):
        self.fecha_actualizacion = fecha_actualizacion
        self.provincias = []  
        self.lugares = []    

    def agregar_provincia(self, provincia):
        self.provincias.append(provincia)

    def agregar_lugar_votacion(self, lugar):
        self.lugares.append(lugar)

    def buscar_lugar(self, codigo):
        for lugar in self.lugares:
            if lugar.codigo == codigo:
                return lugar
        return None

    def consultar_lugar_votacion(self, provincia_nombre, dni):
        for provincia in self.provincias:
            if provincia.nombre == provincia_nombre:
                for votante in provincia.votantes:
                    if votante.dni == dni:
                        lugar = self.buscar_lugar(votante.codigo_lugar)
                        if lugar:
                            resultado = {
                                "nombre": votante.nombre,
                                "direccion": lugar.direccion,
                                "localidad": lugar.localidad,
                                "mesa": votante.mesa
                            }
                            return True, resultado
        return False, {}