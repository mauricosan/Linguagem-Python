# Crie um programa que solicita do usuário um valor N representando a
# quantidade linhas e um valor M representando a quantidade de colunas
# de uma matriz. Depois, o programa deverá solicitar do usuário N x M
# elementos para serem incluídos na matriz. Por fim, o programa deverá
# percorrer a matriz para encontrar e imprimir o seu maior elemento e o
# seu menor elemento.

linhas = int(input("Digite a quantidade de linhas da matriz: "))
colunas = int(input("Digite a quantidade de colunas da matriz: "))


matriz = []

i = 0
while i < linhas:
    linha = []  
    j = 0
    while j < colunas:
        valor = int(input(f"Digite o elemento [{i+1},{j+1}]: "))
        linha.append(valor)
        j += 1
    matriz.append(linha)  
    i += 1

print("Matriz completa:")
print(matriz)

maior = matriz[0][0]
menor = matriz[0][0]

i = 0
while i < linhas:
    j = 0
    while j < colunas:
        if matriz[i][j] > maior:
            maior = matriz[i][j]
        if matriz[i][j] < menor:
            menor = matriz[i][j]
        j += 1
    i += 1

print("Maior elemento:", maior)
print("Menor elemento:", menor)

