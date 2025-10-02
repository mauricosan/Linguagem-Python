# 7. Faça um programa em Python que leia um conjunto de valores
# correspondentes às notas que os alunos obtiveram em uma prova de
# Algoritmos. Quando o valor fornecido for um número negativo, significa
# que não existem mais notas para serem lidas. Após isso seu programa
# deverá:
#  Escrever quantas notas são maiores ou iguais a 6.0
#  Escrever quantas notas são maiores ou iguais a 4.0 e menores que 6.0
#  Escrever quantos notas são menores que 4.0
#  Escrever a média das notas fornecidas pelo usuário.


cont_maior_6 = 0
cont_entre_4_e_6 = 0
cont_menor_4 = 0

soma_notas = 0
quantidade = 0


nota = float(input("Digite a nota do aluno (valor negativo para parar): "))

while nota >= 0:  
    if nota >= 6.0:
        cont_maior_6 += 1
    elif nota >= 4.0:
        cont_entre_4_e_6 += 1
    else:
        cont_menor_4 += 1

    soma_notas += nota
    quantidade += 1

    
    nota = float(input("Digite a nota do aluno (valor negativo para parar): "))


print(f"Notas maiores ou iguais a 6.0: {cont_maior_6}")
print(f"Notas entre 4.0 e 6.0: {cont_entre_4_e_6}")
print(f"Notas menores que 4.0: {cont_menor_4}")

if quantidade > 0:
    media = soma_notas / quantidade
    print(f"Média das notas: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")
