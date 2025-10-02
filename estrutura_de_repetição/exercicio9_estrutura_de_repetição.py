# Elabore um programa que efetue a soma de todos os números ímpares que são
# # múltiplos de 3 e que se encontram no intervalo de 1 a 500. 

cont = 0
soma = 0

while cont < 501:
    if cont %2==1 and cont  %3==0:
        soma += cont
        print(cont)
    cont +=1

print (f"A soma dos números impáres e multiplos de 3 é: {soma} ")
