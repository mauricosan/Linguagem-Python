# Crie um programa que leia inicialmente uma sequência de N números
# inteiros. Depois, o programa deve gerar e mostrar 2 novas listas a
# partir da primeira: uma sem repetição de elementos e outra com os
# elementos que se repetem na lista original.

qnt = int(input("Digite a quantidade de elementos: "))
cont = 0

n = 1

lista_sem_rep = []
lista_rep = []
lista_ori = []

while cont < qnt:
    n1 = int(input(f"Digite o {n}° número da lista: "))
    lista_ori.append(n1)
    n += 1
    cont += 1
print("Lista original:", lista_ori, "\n")

cont = 0
while cont < qnt:
    elemento = lista_ori[cont]
    j = 0
    repetido = False

    while j < qnt:
        if j != cont and lista_ori[j] == elemento:
            repetido = True
        j += 1

    if repetido:
        if elemento not in lista_rep:
            lista_rep.append(elemento)
    else:
        lista_sem_rep.append(elemento)

    cont += 1

print("Lista sem repetição:", lista_sem_rep)
print("Lista de repetidos:", lista_rep)