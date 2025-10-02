# 1. Gere uma lista contendo os múltiplos de 3 entre 1 e 150.

lista = []
cont = 0

while cont < 150:
    if cont < 151 and cont %3==0:
        lista.append(cont)
    cont +=1

print (lista)