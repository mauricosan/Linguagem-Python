# Faça um programa que calcule e apresente o mmc entre dois números

def calcular_mmc(a, b):
    def mdc(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    
    return (a * b) // mdc(a, b)


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))


resultado = calcular_mmc(num1, num2)
print(f"O MMC entre {num1} e {num2} é: {resultado}")
