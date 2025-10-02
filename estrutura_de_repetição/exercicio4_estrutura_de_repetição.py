# 4. Faça um programa para mostrar as tabuadas de todos os números de 1
# a 10

i = 1
tabuada = 0

while i < 11:
    j = 0

    while j < 11:
        tabuada = i * j
        print(f"{i} x {j} = {tabuada}")
        j+=1
    print()
    i+=1    