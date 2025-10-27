# Escreva um programa que remove a primeira ocorrência de uma letra de
# uma string. A string e a letra devem ser fornecidas pelo usuário.


string = input("Digite uma frase: ")
letra = input("Qual letra deseja remover?: ")

removida = False
i = 0
nova_string = ""

while i < len(string):
    if string[i] == letra and not removida:
        removida = True
    else:
        nova_string += string[i]
    i +=1

print(nova_string)

