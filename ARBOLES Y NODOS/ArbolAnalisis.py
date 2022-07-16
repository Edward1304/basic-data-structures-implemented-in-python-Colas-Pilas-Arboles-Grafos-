
import operator
from Clase_ArbolBinario import *
from ClassPila import Pila
from  RecorridosArboles import *




def construirArbolAnalisis(expresionAgrupada):
    listaSimbolos = expresionAgrupada.split()
    pilaPadres = Pila()
    arbolExpresion = ArbolBinario('')
    pilaPadres.incluir(arbolExpresion)
    arbolActual = arbolExpresion
    for i in listaSimbolos:
        if i == '(':
            arbolActual.insertarIzquierdo('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoIzquierdo()
        elif i not in ['+', '-', '*', '/', ')']:
            arbolActual.asignarValorRaiz(int(i))
            padre = pilaPadres.extraer()
            arbolActual = padre
        elif i in ['+', '-', '*', '/']:
            arbolActual.asignarValorRaiz(i)
            arbolActual.insertarDerecho('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoDerecho()
        elif i == ')':
            arbolActual = pilaPadres.extraer()
        else:
            raise ValueError
    return arbolExpresion

miArbolAnalisis = construirArbolAnalisis("( ( 10 + 5 ) * 3 )")
print(miArbolAnalisis) 
preorden(miArbolAnalisis)
inorden(miArbolAnalisis)
postorden(miArbolAnalisis)




def evaluar (arbolAnalisis):
    operadores ={'+':operator.add,'-':operator.sub,
    '*':operator.mul,'/':operator.truediv}

    hijoizquierdo = arbolAnalisis.obtenerHijoIzquierdo()
    hijoDerecho = arbolAnalisis.obtenerHijoDerecho()

    if hijoizquierdo and hijoDerecho:
        fn=operadores[arbolAnalisis.obtenerValorRaiz()]
        return fn(evaluar(hijoizquierdo),evaluar(hijoDerecho))
    else:
        return arbolAnalisis.obtenerValorRaiz()


print(evaluar(miArbolAnalisis))

