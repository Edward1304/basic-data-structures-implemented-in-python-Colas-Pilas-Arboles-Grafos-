
from programa_3_14_modidicado import ColaDoble
def verificarPalindromo(cadena):

    colaDobleCaracteres = ColaDoble()
    for  caracter in cadena:
        if caracter != " ":                              #modificacion  para que reconozca espacio
           colaDobleCaracteres.agregar(caracter,"final")

    aunIguales = True

    while colaDobleCaracteres.tamano() > 1 and aunIguales:
        primero = colaDobleCaracteres.remover("frente")
        ultimo = colaDobleCaracteres.remover("final")
        if primero != ultimo:
            aunIguales = False

    return aunIguales

print(verificarPalindromo("lsdkjfskf"))
print(verificarPalindromo("radar"))
print(verificarPalindromo("anita lava la tina"))
