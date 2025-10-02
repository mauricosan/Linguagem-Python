#  Crie um programa que leia inicialmente uma sequência de N notas de
# alunos fornecidas pelo usuário e ao final mostre a sequência e sua
# média aritmética. Defina um critério de parada para a entrada de
# notas pelo usuário.

lista = []
posi = 1
soma = 0

aluno = input(f"Digite a {posi}° nota(ENTER P/ PARAR): ")
posi += 1

while aluno != "":
    aluno = float(aluno)
    lista.append(aluno)
    soma += aluno

    aluno = input(f"Digite a {posi}° nota(ENTER P/ PARAR): ")
    posi += 1

if len(lista) > 0:
    media = soma / len(lista)
    print(f"Notas digitadas: {lista}")
    print(f"Média aritmética: {media:.2f}")
else:
    print("Nenhuma nota foi digitada.")
