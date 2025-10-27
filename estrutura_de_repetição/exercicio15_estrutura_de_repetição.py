# Fazer um programa que apresenta o total da soma dos números pares até 100 (2
# + 4 + 6 + ... + 98 + 100)

i = 0
soma = 0

while i <=100:
    if i %2 == 0:
        soma +=i
    i+=1

print(soma)
