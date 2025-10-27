# Escreva um programa que remove todas as ocorrências de uma letra de
# uma string. A string e a letra devem ser fornecidas pelo usuário.


string = input("Digite uma string: ")
letra = input("Qual letra deseja remover?: ")

new_string = ""
i = 0

while i < len(string):
    if string[i] != letra:
        new_string += string[i]
    i += 1

print(new_string)

