from src.Metodos import Votante, Lugar, PadronElectoral, Provincia, Fecha
import random

def prueba():
    fecha = Fecha(2025,4,26)
    Eleccion = PadronElectoral(fecha=fecha)
    for i in range(1, 11):
        provincia = Provincia()
        Eleccion.agregar_provincias(provincia)
        for i in range(1,5):
            lugar = Lugar()
            Eleccion.agregar_lugar_votacion(lugar)
    lugares = Eleccion.lista_lugares
    provincias = Eleccion.lista_provincias
    codigos_lugares =  [lugar.codigo_lugar_votacion for lugar in lugares]
    for i in range(1,26):
        provincia_random = random.choice(provincias)
        provincia_random.agregar_votante(Votante(codigos_lugares))
    
    dnis = []
    
    for provincia in Eleccion.lista_provincias:
        print(f"Provincia: {provincia.nombre}")
        if hasattr(provincia, 'votantes'):
            for votante in provincia.votantes:
                print(f" - {votante.nombre} ({votante.dni})")
                dnis.append(votante.dni)
    else:
        print(" - No tiene votantes asignados aún.")

    provincia_random = random.choice(provincias)
    dni_random = random.choice(dnis)
    print(f'Se buscara al votante con el dni {dni_random} en la provincia {provincia_random.nombre}')
    VoF, registro = Eleccion.Consultar_Lugar_Votacion(provincia_random, dni_random, lugares)

    if VoF:
        print(f"Votante encontrado: {registro}")
    else:
        print("Votante no encontrado en esta provincia.")

if __name__ == "__main__":
    prueba()