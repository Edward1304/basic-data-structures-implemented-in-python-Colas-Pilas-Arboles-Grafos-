


from Clase_ArbolBinario import *
from RecorridosArboles import *



"""
libro = ArbolBinario("libro")
libro.insertarIzquierdo("seccion1.1")
libro.insertarIzquierdo("seccion1")
libro.insertarDerecho("seccio 2.2.2")
libro.insertarDerecho("seccion 2.2")
libro.insertarDerecho("capitulos2")
libro.obtenerHijoIzquierdo().insertarDerecho("seccion 1.2.2")
libro.obtenerHijoIzquierdo().insertarDerecho("seccion 1.2")
libro.obtenerHijoIzquierdo().obtenerHijoDerecho().insertarIzquierdo("seccion 1.2")
libro.obtenerHijoDerecho().insertarIzquierdo("seccion 2.1")
libro.obtenerHijoDerecho().insertarIzquierdo("seccion 2.2.1")


print("recorrido en preorden:")
preorden(libro)
print("recorrido en  inorden: ")
inorden(libro)
print("recorrido en postorden")
postorden(libro)
"""



A = ArbolBinario("A")
A.insertarIzquierdo("k")
A.insertarIzquierdo("G")
A.insertarIzquierdo("D")
A.insertarIzquierdo("B")
A.obtenerHijoIzquierdo().insertarDerecho("L")
A.obtenerHijoIzquierdo().obtenerHijoIzquierdo().insertarDerecho("H")
A.obtenerHijoIzquierdo().insertarDerecho("E")
A.insertarDerecho("C")
A.obtenerHijoDerecho().insertarIzquierdo("F")
A.obtenerHijoDerecho().obtenerHijoIzquierdo().insertarDerecho("I")
A.obtenerHijoDerecho().obtenerHijoDerecho().insertarIzquierdo("J")
A.obtenerHijoDerecho().obtenerHijoIzquierdo().obtenerHijoIzquierdo().insertarIzquierdo("M")
A.obtenerHijoIzquierdo().obtenerHijoIzquierdo().obtenerHijoIzquierdo().insertarDerecho("N")
print("recorrido en preorden:")
preorden(A)
print("recorrido en  inorden: ")
inorden(A)
print("recorrido en postorden")
postorden(A)



