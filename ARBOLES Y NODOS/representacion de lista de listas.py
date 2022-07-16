


from cgi import print_form


miArbol = ['a',   #raíz
      ['b',  #subárbol izquierdo 
       ['d', [], []],
       ['e', [], []] ],
      ['c',  #subárbol derecho
       ['f', [], []],
       [] ]
     ]

miArbol = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]

print(miArbol[2][1][0]) 

