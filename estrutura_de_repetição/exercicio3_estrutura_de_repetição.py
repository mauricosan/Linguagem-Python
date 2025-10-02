# 3. Faça um programa para mostrar a tabuada de um número qualquer
# fornecido pelo usuário. Por exemplo, se o número fornecido for igual a
# 3, o programa de apresentar a seguinte saída:

numero = int(input("Digite o numero que deseja a tabuada: "))

i = 0
multiplição = 0
while i < 11:
    multiplição = numero * i
    print(f"{numero} x {i} = {multiplição}")
    i+=1