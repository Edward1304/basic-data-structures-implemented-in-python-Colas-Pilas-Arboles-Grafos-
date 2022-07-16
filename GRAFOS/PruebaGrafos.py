from Progrma_7_02 import *

g = Grafo()
g.agregarArista("Vo",1,5)
g.agregarArista("v1",5,2)
g.agregarArista("V0",2,4)
g.agregarArista("v2",3,9)
g.agregarArista("V0",4,7)
g.agregarArista("V2",5,3)
g.agregarArista(4,0,1)
g.agregarArista(5,4,8)
g.agregarArista(5,2,1)
for i in range(6):
    print(g.listaVertices)

for v in g:
    for w in v.obtenerConexiones():
        print("( %s , %s )" % (v.obtenerId(), w.obtenerId(), ) )
        