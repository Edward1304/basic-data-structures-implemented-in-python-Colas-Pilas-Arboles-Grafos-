

from VerficarSimbolos import verificarSimbolos

verificacion =  verificarSimbolos("{{(a[][a+b])}}")
if verificacion :
    print("los simbolos estan balanceados")
else:
    print("los simbolos  no estan balanceados")
    