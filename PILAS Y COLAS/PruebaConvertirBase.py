


from ConvertirBase import convertirBase


numeroDecimal = 4579
cadenaOCtal = convertirBase(numeroDecimal, 8)
cadenaDoce =  convertirBase(numeroDecimal, 12)
cadenaHexadecimal = convertirBase(numeroDecimal, 16)
cadenaSexagecimal = convertirBase(numeroDecimal, 60)


print("El numero",numeroDecimal,"en octal es : ",cadenaOCtal,\
    "y en cadena hexadecimal es: ", cadenaHexadecimal)

print("el numero",numeroDecimal, "en sexadecimal es : ",cadenaSexagecimal)


