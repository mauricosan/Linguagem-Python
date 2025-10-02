# 6. Faça um programa em Python que receba dois valores inteiros,
# representando a base e o expoente. O programa deverá calcular e
# apresentar o resultado da base elevada ao expoente. Por exemplo, para
# base = 5 e expoente = 3, ou seja, 53
# , o programa deverá imprimir 125.
#  Obs: não utilize o operador de exponenciação (**). Utilize somente estrutura de
# repetição.

inicio = input("Deseja iniciar? (S/N): ").upper()
calculo = 0

while inicio == "S":
    base = int(input("Digite o valor da base: "))
    expoente = int(input("Digite o valor do expoente: "))

    resultado = 1
    i = 0

    while i < expoente:
        resultado *= base
        i += 1

    print(f"{base} elevado a {expoente} é {resultado}")
    inicio = input("Deseja realizar outro cálculo? (S/N): ").upper()

print("Programa encerrado.")


