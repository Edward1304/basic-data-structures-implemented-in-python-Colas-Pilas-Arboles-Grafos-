

def aCadena(n, base):
    cadenaConversion  = "0123456789ABCDEF"
    if n < base :
        return cadenaConversion[n]
    else:
       # return aCadena(n//base,base) +  cadenaConversion[n % base]
       return cadenaConversion[n % base] + aCadena(n//base,base)


print(aCadena(769, 10))
print(aCadena(769, 2))
print(aCadena(769, 16))