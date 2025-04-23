from src.Metodos import Votante, LugarVotacion, Padron2025, Provincia



def prueba():
    padron = Padron2025("2025-04-12")

    padron.agregar_lugar_votacion(LugarVotacion("L001", "Av. Central 123", "San Juan"))
    padron.agregar_lugar_votacion(LugarVotacion("L002", "Calle Sur 456", "Mendoza"))

    prov_sj = Provincia("San Juan")
    prov_sj.votantes.append(Votante("12345678", "Freddy Pérez", "L001", "Mesa 15"))
    padron.agregar_provincia(prov_sj)

    encontrado, datos = padron.consultar_lugar_votacion("San Juan", "12345678")
    if encontrado:
        print("Votante:", datos["nombre"])
        print("Dirección:", datos["direccion"])
        print("Localidad:", datos["localidad"])
        print("Mesa:", datos["mesa"])
    else:
        print("Votante no encontrado.")

if __name__ == "__main__":
    prueba()