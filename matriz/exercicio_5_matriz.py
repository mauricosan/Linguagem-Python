# Escreva um programa que leia inteiros positivos m e n e os elementos
# de uma matriz A de números inteiros de dimensão m x n e ao final
# mostra a quantidade de linhas e colunas que tem apenas zeros (linhas
# nulas e colunas nulas).

# Lê as dimensões da matriz
m = int(input("Digite o número de linhas: "))
n = int(input("Digite o número de colunas: "))


matriz = []
i = 0
while i < m:
    linha = []
    j = 0
    while j < n:
        valor = int(input(f"Digite o elemento [{i+1},{j+1}]: "))
        linha.append(valor)
        j += 1
    matriz.append(linha)
    i += 1


linhas_nulas = 0
i = 0
while i < m:
    todos_zeros = True
    j = 0
    while j < n:
        if matriz[i][j] != 0:
            todos_zeros = False
        j += 1
    if todos_zeros:
        linhas_nulas += 1
    i += 1

colunas_nulas = 0
j = 0
while j < n:
    todos_zeros = True
    i = 0
    while i < m:
        if matriz[i][j] != 0:
            todos_zeros = False
        i += 1
    if todos_zeros:
        colunas_nulas += 1
    j += 1


print(f"\nQuantidade de linhas nulas: {linhas_nulas}")
print(f"Quantidade de colunas nulas: {colunas_nulas}")
