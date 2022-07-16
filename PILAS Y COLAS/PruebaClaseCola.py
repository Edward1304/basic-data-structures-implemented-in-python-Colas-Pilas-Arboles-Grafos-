

from ClassCola import Cola

c = Cola()

print(c.estaVacia())
c.agregar("perro")
c.agregar(4)
c = Cola()
print(c.estaVacia())
c.agregar(4)
c.agregar("perro")
c.agregar(True)
print(c.tamano())
c.agregar(8.4)
print(c.avanzar)
print(c.avanzar())
print(c.tamano)
