# 5. Faça um programa que receba um número inteiro maior que 1,
# verifique se o número é primo ou não e mostre a mensagem de
# número primo ou de número não primo. Obs: Um número é primo
# quando é divisível apenas por 1 e por ele mesmo.

numero = input("Digite um número (ENTER PARA PARAR): ")

while numero != "":
    inteiro = int(numero)

    if inteiro > 1:
        i = 2
        primo = True

        while i < inteiro:
            if inteiro % i == 0:
                primo = False
            i += 1

        if primo:
            print("Número primo")
        else:
            print("Número não primo")
    else:
        print("Número não primo")

    numero = input("Digite um número (ENTER PARA PARAR): ")

print("Programa encerrado.")
