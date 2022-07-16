from VerificarParentesis import verificarParentesis

verificacion = verificarParentesis("(a+b)")
if verificacion:
    print("Los paréntesis están balanceados")
else:
    print("Los paréntesis no están balanceados")
