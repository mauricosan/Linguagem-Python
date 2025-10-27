# 2. Elabore um programa para armazenar uma agenda de telefones em um dicionário. Cada
# pessoa pode ter um ou mais telefones e a chave do dicionário será o nome da pessoa. O
# programa deve implementar as seguintes funções:

# a) incluirContato() – essa função acrescenta um novo nome na agenda, com um ou mais
# telefones. Ela deve receber como argumento o nome do novo contato. Caso o contato não
# exista na agenda, a função deverá inseri-lo e depois deve retornar 1, indicando que a
# inclusão foi bem sucedida. Caso contrário, a função deverá retornar 0. A mensagem
# informando se a inclusão ocorreu ou não, deve ser impressa no programa principal;

# b) incluirTelefone() – essa função acrescenta um telefone em um contato já existente na
# agenda. Caso o contato não exista, a função deverá retornar 0. Caso existe, a função deverá
# retornar 1 indicando que a inclusão foi bem sucedida;

# c) excluirTelefone() – essa função deve receber como parâmetro o nome do contato e o
# telefone a ser removido. Se o nome estiver na agenda e o telefone estiver cadastrado, a
# função deverá remover o telefone e retornar 1. Caso contrário, deverá retornar 0;

# d) excluirNome() – essa função deverá receber como parâmetro o nome do contato, excluir
# o contato e retornar 1, indicando que a exclusão foi bem sucedida. Caso contrário, a função
# deverá retornar 0.

# e) consultarTelefone() – essa função deverá receber como parâmetro o nome do contato e
# imprimir todos os seus telefones ou uma mensagem indicando que o contato não existe.

# f) imprimirContatos() - essa função deve imprimir cada contato da agenda e todos os seus
# telefones (use um laço de repetição para percorrer cada item do dicionário)


def menu_opções():
    print("\n--- MENU DE OPÇÕES ---")
    print("1 - Incluir contato")
    print("2 - Incluir telefone")
    print("3 - Excluir telefone")
    print("4 - Excluir nome")
    print("5 - Consultar telefone")
    print("6 - Imprimir contato")
    print("7 - Sair")
    return int(input("Escolha uma opção: "))

def incluir_contato(agenda, nome):
    if nome in agenda:
        return  False
    
    zapzap = []
    continuar = True

    while continuar:
        telefone = input("Digite um número de telefone. (ENTER P/PARAR): ")

        if telefone == "":
            continuar = False
        
        else:
            zapzap.append(telefone)

    agenda[nome] = zapzap
    return True

def incluir_telefone(agenda, nome, telefone):
    if nome in agenda:
        agenda[nome].append(telefone)
        return True
    return False

def excluir_telefone(agenda, nome):
    if nome in agenda:
        if len(agenda[nome]) == 0:
            print("Esse contato não possui telefones cadastrados.")
            return False

        print(f"\ntelefones de {nome}:")
        i = 0
        while i < len(agenda[nome]):
            print(f"{i+1}. {agenda[nome][i]}")
            i += 1

        indice = int(input("Digite o número do telefone que deseja excluir: ")) - 1

        if indice >= 0 and indice < len(agenda[nome]):
            del agenda[nome][indice]
            return True
        else:
            print("Número invalido.")
            return False
    else:
        print("Contato não encontrado.")
        return False

def excluir_nome(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        return True
    return False 

    
def consultar_telefone(agenda, nome):
    if nome in agenda:
        print(f"Telefone de {nome} :")
        for i in agenda[nome]:
            print("--",i)
    else:
        print("Contato não encontrado!.")

def imprimir_contato(agenda):
    if len(agenda) == 0:
        print("Agenda vazia.")
    else:
        for nome in agenda:
            print("\nContato", nome)
            for tel in agenda[nome]:
                print("--", tel)

def main():
    agenda = {}
    opcao = 1
    while opcao != 7:
        opcao = menu_opções()

        if opcao == 1:
            nome = input("Digite o nome do contato: ")
            if incluir_contato(agenda, nome) == 1:
                print("Contato inserido.")
            else:
                print("Contato já existe.")

        elif opcao == 2:
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone que deseja adicionar: ")
            if incluir_telefone(agenda, nome, telefone) == 1:
                print("Telefone adicionado.")
            else:
                print("Contato não encontrado.")

        elif opcao == 3:
            nome = input("Digite o nome do contato: ")
            if excluir_telefone(agenda, nome):
                print("Telefone excluido.")
            else:
                print("Contato ou telefone não encontrado.")

        elif opcao == 4:
            nome = input("Digite o nome do contato: ")
            if excluir_nome(agenda, nome) == 1:
                print("Contato excluido.")
            else:
                print("Contato não encontrado.")

        elif opcao == 5:
            nome = input("Digite o nome do contato: ")
            consultar_telefone(agenda, nome)

        elif opcao == 6:
            imprimir_contato(agenda)

        elif opcao == 7:
            print("Programa encerrado.")

        else:
            print("Opção inválida, tente novamente.")
         


main()