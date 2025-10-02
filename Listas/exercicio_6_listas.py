# Crie um programa que dada uma sequência de N elementos fornecidos
# pelo usuário mostre a sequência original e a sequência elevada ao cubo.

seq = int(input("Digite a quantidade de elementos: "))
cont = 0
n = 1 


list_ori = []
lista_cubo = []

while cont < seq:
    num = int(input(f"Digite o {n}° número: "))
    list_ori.append(num)
    cont +=1
    n +=1
print("Lista original:",list_ori,"\n")


cont = 0
while cont < seq:
    lista_cubo.append(list_ori[cont] ** 3)
    cont +=1

print(lista_cubo)
