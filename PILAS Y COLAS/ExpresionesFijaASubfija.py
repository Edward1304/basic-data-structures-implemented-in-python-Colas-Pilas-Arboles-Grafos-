

import string
from ClassPila import Pila

import string

def  infija_a_sufija(expresionInfija):
    precendencia = {}
    precendencia ["*"]= 3
    precendencia["/"]= 3
    precendencia["+"]= 2
    precendencia["-"]= 2
    precendencia["("]= 1
    pilaOperadores = Pila()
    listaSufija = []
    listaSimbolos = expresionInfija.split()
    for simbolo in listaSimbolos:
        if simbolo in string.ascii_uppercase or simbolo.isdigit():
            listaSufija.append(simbolo) 
        elif simbolo == '(':
            pilaOperadores.incluir(simbolo)
        elif simbolo ==')':
            simboloTope = pilaOperadores.extraer()
            while simboloTope != '(':
                listaSufija.append(simboloTope)
                simboloTope  = pilaOperadores.extraer()
        
        else:
             while (not pilaOperadores.estaVacia()) and \
                (precendencia[pilaOperadores.inspeccionar()] >=  \
                 precendencia[simbolo]):
                  listaSufija.append(pilaOperadores.extraer())
        
             pilaOperadores.incluir(simbolo)
    
    while not pilaOperadores.estaVacia():
        listaSufija.append(pilaOperadores.extraer())
    return "  ".join(listaSufija )


                


            


