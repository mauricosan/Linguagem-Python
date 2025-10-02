# A turma do colégio vai fazer uma excursão na serra e todos os alunos e
# monitores vão tomar um teleférico para subir até o pico de uma
# montanha. A cabine do teleférico pode levar C pessoas no máximo,
# contando alunos e monitores, durante uma viagem até o pico. Por
# questão de segurança, tem que ter pelo menos um monitor dentro da
# cabine junto com os alunos. Por exemplo, se cabem C=10 pessoas na
# cabine e a turma tem A=20 alunos, o colégio poderia fazer três viagens:
# a primeira com 8 alunos e um monitor; a segunda com 6 alunos e um
# monitor; e a terceira com 6 alunos e um monitor. Você consegue ver que
# não seria possível fazer apenas duas viagens?

# Dados como entrada a capacidade C da cabine e o número total A de
# alunos, você deve escrever um programa para calcular o número
# mínimo de viagens do teleférico.

cabine = int(input("Quantas pessoas cabem no teleférico?: "))
alunos = int(input("Quantos alunos irão para a serra?: "))

viagens_por_cabine = cabine - 1


viagem = alunos // viagens_por_cabine

if alunos % viagens_por_cabine != 0:   
    viagem += 1

print(f"Serão necessarias {viagem} viagens.")

    



