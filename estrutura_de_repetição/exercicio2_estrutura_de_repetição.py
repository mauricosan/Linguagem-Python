# 2. Faça um programa que exiba todos os números de 1 a 100 que são
# divisíveis por 7 e por 3.

i  = 0
while i < 100:
    if i %3 == 0:
        print(f"Divisivel por 3: {i}")
    i+=1

print()

i  = 0
while i < 100:
    if i %7 == 0:
        print(f"Divisivel por 7: {i}")
    i+=1