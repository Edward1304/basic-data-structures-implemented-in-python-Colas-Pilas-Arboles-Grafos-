from ClassPila import Pila

def convertirBase (numeroDecimal, base):
    digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    pilaResiduo = Pila()

    while  numeroDecimal > 0:
        residuo = numeroDecimal % base
        pilaResiduo.incluir(residuo)
        numeroDecimal =  numeroDecimal // base

    nuevaCadena = ""

    while not pilaResiduo.estaVacia():
        nuevaCadena = nuevaCadena +  digitos [pilaResiduo.extraer()]
    return nuevaCadena