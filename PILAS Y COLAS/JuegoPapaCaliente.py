from random import  randrange
from ClassCola import Cola

def papaCaiente(listaNombres):
   
    colaSimulacion = Cola()
    for nombre in listaNombres:
        colaSimulacion.agregar(nombre)
    
    while colaSimulacion.tamano() > 1:
        N= randrange(100)

        for i in range(N):
            colaSimulacion.agregar(colaSimulacion.avanzar())

        print(colaSimulacion.avanzar())

    return colaSimulacion.avanzar()


jugadores= ["Bill","David","Susan","Jane","kent","Brand"]

print(papaCaiente(jugadores))




