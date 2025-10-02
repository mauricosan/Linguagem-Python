# Faça um programa que solicite do usuário os elementos de uma matriz 3
# x 2 (matriz A). Em seguida, o programa deverá criar a matriz transposta
# de A (A
# t
# ). Ao final, deve ser mostrada a matriz original e sua respectiva
# transposta. Lembre-se que a matriz transposta At
#  será obtida a partir da
# matriz A trocando-se ordenadamente as linhas por colunas (ou as
# colunas por linhas), como no exemplo a seguir:


linhas = 3
colunas = 2


matriz = []
i = 0
while i < linhas:
    linha = []
    j = 0
    while j < colunas:
        valor = int(input(f"Digite o elemento [{i+1},{j+1}] da matriz A: "))
        linha.append(valor)
        j += 1
    matriz.append(linha)
    i += 1


transposta = []
j = 0
while j < colunas:
    linha_transposta = []
    i = 0
    while i < linhas:
        linha_transposta.append(matriz[i][j])
        i += 1
    transposta.append(linha_transposta)
    j += 1


print("\nMatriz A:")
i = 0
while i < linhas:
    print(matriz[i])
    i += 1


print("\nMatriz transposta At:")
j = 0
while j < colunas:
    print(transposta[j])
    j += 1
