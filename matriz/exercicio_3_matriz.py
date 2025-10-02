
N = int(input("Digite a dimensão da matriz quadrada: "))


matriz = []
i = 0
while i < N:
    linha = []
    j = 0
    while j < N:
        valor = int(input(f"Digite o elemento [{i+1},{j+1}] da matriz A: "))
        linha.append(valor)
        j += 1
    matriz.append(linha)
    i += 1


simetrica = True
i = 0
while i < N:
    j = 0
    while j < N:
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
        j += 1
    i += 1


print("\nMatriz A:")
i = 0
while i < N:
    print(matriz[i])
    i += 1


if simetrica:
    print("\nA matriz é simétrica.")
else:
    print("\nA matriz não é simétrica.")
