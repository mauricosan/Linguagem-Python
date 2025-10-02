# 1. Faça um programa que receba 5 números inteiros e informe o maior
# entre eles

i = 0
j = 1

while i < 5:
    num1 = int(input(f"Digite o {j}° número: "))

    if i == 0:
        maior = num1
    else:
        if num1 > maior:
            maior = num1
    i+=1
    j+=1

print(f"O maior número é: {maior}")