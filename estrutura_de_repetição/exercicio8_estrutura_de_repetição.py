# Faça um programa que mostre os 8 primeiros termos da sequência de
# Fibonacci. Ex: 0, 1, 1, 2, 3, 5, 8,13, 21,34, 55...


n1 = 0
n2 = 1

print(n1)
print(n2)

cont = 2  

while cont < 11:
    proximo = n1 + n2
    print(proximo)
    n1 = n2
    n2 = proximo
    cont += 1
