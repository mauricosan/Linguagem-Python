# Crie um programa que leia inicialmente uma sequência de N números
# inteiros e ao seu final mostre a sequência original, a soma de seus
# elementos que forem pares e a multiplicação dos elementos que
# forem ímpares.

posi = 1
num = input(f"Digite o {posi}° número(ENTER P/ PARAR): ")
posi += 1

lista = []
soma = 0
multi = 1
tem_impar = False

while num != "":
    num = int(num)
    lista.append(num)

    if num %2 == 0:
        soma += num
    else:
        multi *= num
        tem_impar = True


    posi +=1
    num = input(f"Digite o {posi}° número (ENTER P/ PARAR): ")

print("Sequência digitada:", lista)
print("Soma dos pares:", soma)

if tem_impar:
    print("Multiplicação dos ímpares:", multi)
else:
    print("Nenhum ímpar foi digitado.")