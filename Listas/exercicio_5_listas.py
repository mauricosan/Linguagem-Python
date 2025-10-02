# Crie um programa que leia inicialmente duas sequências de N
# elementos cada uma e ao final mostre as duas sequências originais e a
# sequência resultante da soma de seus elementos. Exemplo:

qnt = int(input("Digite a quantidade de elementos: "))
cont = 0

n = 1

lista_a = []
lista_b = []
soma_listas = []

while cont < qnt:
    n1 = int(input(f"Digite o {n}° número da lista A: "))
    lista_a.append(n1)
    n += 1
    cont += 1
print("Lista A:", lista_a, "\n")


cont = 0
n = 1
while cont < qnt:
    n2 = int(input(f"Digite o {n}° número da lista B: "))
    lista_b.append(n2)
    n += 1
    cont += 1
print("Lista B:", lista_b, "\n")

cont = 0
while cont < qnt:
    soma_listas.append(lista_a[cont] + lista_b[cont])
    cont += 1

print("Soma das listas:", soma_listas)
