#  Crie um programa que leia inicialmente uma sequência de N elementos
# inteiros positivos fornecidos pelo usuário e substitua seus elementos de
# valor ímpar por -1 e os pares por +1. Ao final imprima a sequência
# original e a sequência alterada


seq = int(input("Digite a quantidade de elementos: "))

n = 1
cont = 0
lista_ori = []
lista_alt = []

while cont < seq:
    num = int(input(f"Digite o {n} número: "))

    if num < 0:
        print("\nDIGITE UM NÚMERO POSITIVO!\n")
        num = int(input(f"Digite o {n} número: "))
    lista_ori.append(num)

    n += 1
    cont +=1

print("Lista original:",lista_ori,"\n")


cont = 0

while cont < seq:
    if lista_ori [cont]%2 == 0:
        lista_alt.append(1)
    else:
        lista_alt.append(-1)
    cont +=1
print("Lista alterada:", lista_alt)
    