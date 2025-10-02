# 2. Faça um programa que receba a idade de um eleitor e informa se o
# voto dele é facultativo (entre 16 e 17 anos), obrigatório (entre 18 a 65),
# se ele está dispensado de votar (acima de 65) ou ainda se ele não tem
# idade para votar.

def entrada():
    idade = int(input("Digite sua idade: "))
    return idade

def verificar_maioridade ():
    idade = entrada()

    if idade >= 16 and idade <= 17:
        print("Seu voto é facultativo.")

    elif idade >= 18 and idade <=65:
        print("Seu voto é obrigatório.")
    else:
        print("Dispensado de votar.")

verificar_maioridade()

    