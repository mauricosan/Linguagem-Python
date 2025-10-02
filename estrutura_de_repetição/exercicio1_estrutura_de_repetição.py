# 1. Faça um programa que exiba todos os números de 1 a 100 que são
# divisíveis por 7.

i = 0

while i <100:
    if i %7==0:
        print(f"Número divisivel por 7: {i}")
    i+=1