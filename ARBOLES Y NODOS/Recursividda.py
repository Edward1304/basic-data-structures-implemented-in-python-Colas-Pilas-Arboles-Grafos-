

from traceback import print_tb
from typing import Iterable


def  sumaLista(numLista):
    if len(numLista) == 1 :
        
        return numLista[0]
    else:
        return numLista[0]+sumaLista(numLista[1:])


#print(sumaLista([1,3,5,7,9]))
        


def  factorialRecursivo(n):
    if n ==1:
      return 1
    else:
        return  n *factorialRecursivo(n-1)


#print(factorialRecursivo(5))


def factorilIterativo(n):
    productoria =1

    for i in range(1,n+1):
        productoria*= i
    return productoria

#print(factorilIterativo(5))


def combinatoria(n ,r):
    num = factorialRecursivo(n)
    den = factorialRecursivo(r) * factorialRecursivo(n-r)

    return (num / den)



#print(combinatoria(7,4))
    

ls=[]
def fibonacci(n):

    ls.append(1)
    
    if n < 2:
        return n

    else: 
        print("f",n-1," + ","f",n-2)
        return fibonacci(n-1) + fibonacci(n-2)





print(fibonacci(8))
print(sum(ls)-1)    