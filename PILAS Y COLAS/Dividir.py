from ClassPila import Pila

def dividirPor2 (numeroDecimal):
    pilaResiduo = Pila()

    while  numeroDecimal > 0:
        residuo = numeroDecimal % 2
        pilaResiduo.incluir(residuo)
        numeroDecimal =  numeroDecimal // 2

    cadenaBinaria = ""

    while not pilaResiduo.estaVacia():
        cadenaBinaria = cadenaBinaria +  str (pilaResiduo.extraer())
    return cadenaBinaria