# Crie um programa que leia inicialmente uma sequência de N números
# inteiros fornecidos pelo usuário e mostre ao final da leitura a sequência
# original e a sequência invertida.

seq = int(input("Digite a quantidade de elementos: "))
i = 0
n = 1 

list_ori =[]
list_invertida = []

while i < seq:
    num = int(input(f"Digite o {n}° número: "))
    list_ori.append(num)
    i +=1
    n +=1
print("Lista original:",list_ori,"\n")

i = seq - 1  
while i >= 0:
    list_invertida.append(list_ori[i])
    i -= 1

print("Lista invertida:", list_invertida)