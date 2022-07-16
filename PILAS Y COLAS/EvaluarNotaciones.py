

import imp
from  ClassPila import Pila



def evaluacionNotaSufija(expresionSufija):
    pilaOperadores = Pila()
    listaSimbolos = expresionSufija.split()
    for simbolo in listaSimbolos:
        if simbolo.isdigit() or esFlotante(simbolo):
            pilaOperadores.incluir(float(simbolo))
        else:
            operando2 = pilaOperadores.extraer()
            operando1 = pilaOperadores.extraer()
            resultado = hacerAritmetica(simbolo,operando1,operando2)
            pilaOperadores.incluir(resultado)
    return pilaOperadores.extraer()



def  hacerAritmetica(operador, operadorIzquierda, operadorDerecha):
    if operador == "*":
        return operadorIzquierda * operadorDerecha
    
    elif operador=="/":
        return operadorIzquierda / operadorDerecha
    elif operador == "+":
        return operadorIzquierda + operadorDerecha
    elif operador =="-":
        return operadorIzquierda - operadorDerecha


def esFlotante (parametro):
    try:
        float(parametro)
        return True
    except:
        return False