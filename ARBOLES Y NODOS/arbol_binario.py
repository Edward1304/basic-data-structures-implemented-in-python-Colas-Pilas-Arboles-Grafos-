

def  arbolBinario(r):
    return[r,[],[]]



print(arbolBinario("a"))



def insertarIzquierdo(raiz,nuevaRama):
    t = raiz.pop(1)
    if len(t) > 1:
        raiz.insert(1,[nuevaRama,t,[]])
    else:
        raiz.insert(1,[nuevaRama, [], []])
    return raiz


def insertarderecho(raiz,nuevaRama):
    t = raiz.pop(2)
    if len(t) > 1:
        raiz.insert(2,[nuevaRama,[],t])
    else:
        raiz.insert(2,[nuevaRama, [], []])
    return raiz






