

class ArbolBinario:
    
    def __init__(self, objetoRaiz):
        self.clave = objetoRaiz
        self.hijoIzquierdo = None
        self.hijoDerecho = None

    
    def insertarIzquierdo(self,nuevoNodo):
        if self.hijoIzquierdo == None:
            self.hijoIzquierdo = ArbolBinario(nuevoNodo)
        else:
            t = ArbolBinario(nuevoNodo)
            t.hijoIzquierdo = self.hijoIzquierdo
            self.hijoIzquierdo = t

    def insertarDerecho(self,nuevoNodo):
        if self.hijoDerecho == None:
            self.hijoDerecho = ArbolBinario(nuevoNodo)
        else:
            t = ArbolBinario(nuevoNodo)
            t.hijoDerecho = self.hijoDerecho
            self.hijoDerecho = t

    def obtenerHijoDerecho(self):
        return self.hijoDerecho

    def obtenerHijoIzquierdo(self):
        return self.hijoIzquierdo

    def asignarValorRaiz(self,obj):
        self.clave = obj

    def obtenerValorRaiz(self):
        return self.clave



r = ArbolBinario('a')
print(r.obtenerValorRaiz())
print(r.obtenerHijoIzquierdo())
r.insertarIzquierdo('b')
print(r.obtenerHijoIzquierdo())
print(r.obtenerHijoIzquierdo().obtenerValorRaiz())
r.insertarDerecho('c')
print(r.obtenerHijoDerecho())
print(r.obtenerHijoDerecho().obtenerValorRaiz())
r.obtenerHijoDerecho().asignarValorRaiz('hola')
print(r.obtenerHijoDerecho().obtenerValorRaiz())
 