# Função (a): Retorna o nome dos estudantes que possuem mais de 6 notas
def estudantes_com_mais_de_6_notas():
    with open("estudantes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split()
            nome = partes[0]
            notas = list(map(float, partes[1:]))

            if len(notas) > 6:
                print(f"{nome} possui {len(notas)} notas.")

# Função (b): Calcula a média das notas e imprime nome e média
def media_por_estudante():
    with open("estudantes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split()
            nome = partes[0]
            notas = list(map(float, partes[1:]))
            media = sum(notas) / len(notas)
            print(f"{nome}: média = {media:.2f}")

# Função (c): Calcula a nota mínima e máxima de cada estudante
def nota_min_max_por_estudante():
    with open("estudantes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split()
            nome = partes[0]
            notas = list(map(float, partes[1:]))
            print(f"{nome}: menor = {min(notas)} | maior = {max(notas)}")

# Programa principal
print("Estudantes com mais de 6 notas:")
estudantes_com_mais_de_6_notas()

print("\nMédia de cada estudante:")
media_por_estudante()

print("\nNota mínima e máxima de cada estudante:")
nota_min_max_por_estudante()
