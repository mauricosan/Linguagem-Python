# 4. Faça um algoritmo que receba três valores A, B e C e verifica se
# eles podem ser os comprimentos dos lados de um triângulo. Se
# forem, mostrar se é um triângulo equilátero, isósceles ou escaleno.
# Considere que:
#  Para ser triângulo: cada lado é menor que a soma dos outros dois
# lados.
#  Triângulo equilátero: tem três lados iguais
#  Triângulo isósceles: tem dois lados iguais e um diferente
#  Triângulo escaleno: tem três lados diferentes


lado_a = float(input("Digite o valor do lado A: "))
lado_b = float(input("Digite o valor do lado B: "))
lado_c = float(input("Digite o valor do lado C: "))

if (lado_a < lado_b + lado_c) and (lado_b < lado_a + lado_c) and (lado_c < lado_a + lado_b):

    if lado_a == lado_b and lado_b == lado_c:
        print("Triângulo equilátero.")
    elif lado_a != lado_b and lado_b != lado_c and lado_c != lado_a:
        print("Triângulo escaleno.")
    else:
        print("Triângulo isósceles.")
else:
    print("Os valores fornecidos não podem formar um  triângulo.")
