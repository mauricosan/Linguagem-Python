# Faça um programa que leia três notas de provas de uma turma de 50 alunos (3
# notas para cada aluno). Para cada aluno, o programa deve calcular a média
# ponderada como segue: Média = (nota1*2 + nota2*4 + nota3*3 ) / 10. Além de
# mostrar a média de cada aluno, o programa deve mostrar uma mensagem
# "Aprovado", caso a média seja maior ou igual a 6,0, e uma mensagem
# "Reprovado", caso contrário. Ao final, o programa deve calcular e apresentar a
# média geral da turma. 

aluno = 1 
soma_medias = 0
a = 1


while aluno < 50:
    
    print(f"\n{a}° aluno\n")
    nota_1 = float(input(f"Digite a 1ª nota: "))
    nota_2 = float(input(f"Digite a 2ª nota: "))
    nota_3 = float(input(f"Digite a 3ª nota: "))


    
    while nota_1 > 10 or nota_2 > 10 or nota_3 > 10 or nota_1 < 0 or nota_2 < 0 or nota_3 < 0:
        print("Valor inválido! Digite novamente.")
        nota_1 = float(input("Digite a 1ª nota: "))
        nota_2 = float(input("Digite a 2ª nota: "))
        nota_3 = float(input("Digite a 3ª nota: "))

    media = (nota_1*2 + nota_2*4 + nota_3*3 ) / 10
    print(f"Média do aluno {aluno}: {media:.2f}")

    if media >= 6.0:
        print("Aprovado!")
    else:
        print("Reprovado")
    
    soma_medias += media
    
    a +=1
    aluno +=1
    
media_geral = soma_medias / 50
print(f"Média geral da turma: {soma_medias}")