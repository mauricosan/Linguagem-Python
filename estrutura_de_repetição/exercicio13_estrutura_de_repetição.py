# . Faça um programa que gere aleatoriamente um número entre 0 e 100. Em seguida,
# o programa deve pedir que o usuário tente acertar qual o número gerado. Por
# exemplo, suponha que o programa gere o número 21 e o usuário tente adivinhálo digitando o número 50. O programa deve, então, imprimir a mensagem:
# “Número incorreto, tente um valor menor”. O usuário digita, então, o número 10.
# Após a análise deste número, o programa deverá imprimir a mensagem “Número
# incorreto, tente um valor maior”. O processo deve continuar até que o usuário
# acerte o número gerado pelo programa. O programa deve finalizar informando o
# número de tentativas até o acerto.
# Obs: use a função randint() para gerar o número aleatoriamente. 

from random import randint

numero = randint(0, 100)
tentativas = 0
adivinhar = int(input("Qual foi o número gerado?: ")) 
tentativas+=1


while adivinhar!= numero:
    if adivinhar > numero:
        print("\nNúmero incorreto, digite um número menor.")
    else:
        print("\nNúmero incorreto, digite um número maior.")
    tentativas += 1
    adivinhar = int(input("Tente novamente: "))


print(f"\nParabens! Você acertou. \nO número era: {numero}")
print(f"Número de tentativas do usuário: {tentativas}")



