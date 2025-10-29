from colorama import init, Fore, Style #Biblioteca de cores
init(autoreset=True) #aqui ele reseta as cores a cada print automaticamente

from validate_docbr import CPF


def inicio_do_menu_(): #Função de inicio
    print(Fore.CYAN + Style.BRIGHT + "\n\t🏁 Bem-vindo(a) à Locadora — onde sua jornada começa!")
    
    while True: #um laço de repetição while, que enquanto o usuário não digitar s ou n, vai ficar repetindo.
        escolha_do_sistema = input(Fore.LIGHTMAGENTA_EX + "\tDeseja iniciar o sistema da locadora? (s/n): ").lower()
        if escolha_do_sistema in ["s", "n"]:
            return escolha_do_sistema
        else:
            print(Style.BRIGHT + Fore.RED + "\n\tERRO! Digite apenas 's' ou 'n'.")


def exibir_submenu(titulo, cor, opcoes): #função genérica para os submenus, contendo as linhas envolta do título, cor e o titulo, ele também vai enquadrar o titulo no meio do retângulo.
    largura = len(titulo) + 12
    print(Style.BRIGHT + cor + "\n" + "\t" + "╔" + "═" * largura + "╗")
    print(Style.BRIGHT + cor + "\t║" + f"{titulo:^{largura}}" + "║")
    print(Style.BRIGHT + cor + "\t╚" + "═" * largura + "╝")


    cont = 1 #aqui ele vai imprimir quantas opções você colocar no submenu desejado.
    for opcao in opcoes:
        print(f"\t{cont}. {opcao}")
        cont += 1

    while True:
        try:
            escolha = int(input(Style.BRIGHT + Fore.BLACK + "\tEscolha uma opção: "))
            return escolha
        except ValueError:
            print(Style.BRIGHT + Fore.RED + "\n\tUSE APENAS NÚMEROS VÁLIDOS!")



#---------FUNÇÕES DOS SUBMENUS---------

def submenu_principal():
    return exibir_submenu("MENU DE OPÇÕES", Fore.GREEN, [
        "Submenu de Clientes",
        "Submenu de Veículos",
        "Submenu de Aluguéis",
        "Submenu Relatórios",
        "Encerrar"
    ])

def submenu_clientes():
    return exibir_submenu("SUBMENU DE CLIENTES", Fore.YELLOW, [
        "Adicionar Cliente",
        "Excluir Telefone",
        "Buscar Cliente por CPF ou Nome",
        "Atualizar Cadastro",
        "Excluir Cliente",
        "Listar Clientes",
        "Voltar"
    ])

def submenu_veiculos():
    return exibir_submenu("SUBMENU DE VEÍCULOS", Fore.CYAN, [
        "Adicionar Veículos",
        "Remover Veículos",
        "Buscar Veículos por Código",
        "Atualizar Dados do Veículo",
        "Listar Veículos Disponíveis",
        "Listar Veículos Alugados",
        "Voltar"
    ])

def submenu_alugueis():
    return exibir_submenu("SUBMENU DE ALUGUÉIS", Fore.MAGENTA, [
        "Cadastrar Aluguel",
        "Remover Aluguel",
        "Consultar Aluguel",
        "Atualizar Aluguel",
        "Listar Aluguéis Ativos",
        "Listar Histórico de Aluguéis",
        "Voltar"
    ])

def submenu_relatorio ():
    return exibir_submenu("SUBMENU DE RELATÓRIOS", Fore.BLUE, [
        "Relatório de Clientes",
        "Relatório de Veículos",
        "Relatório de Aluguéis",
        "Voltar"
    ]) 

# ---------FUNÇÕES DAS OPÇÕES DO SUBMENU CLIENTES---------

def cadastrar_clientes_cadastro_de_pessoa_fisica(nome,cpf, agenda):

    if cpf in agenda:
        return False, Style.BRIGHT + Fore.RED + "\tCPF já cadastrado."
    
    if nome in agenda:
        return False, Style.BRIGHT + Fore.RED + "\tCliente já cadastrado."
    
    if not validar_nome(nome):
        return False, Style.BRIGHT + Fore.RED + "\tNome Inválido!"
    
    if not validar_cpf(cpf):
        return False, Style.BRIGHT + Fore.RED + "\tCPF Inválido!"
    
    agenda[cpf] = {"nome": nome}
    return True, Style.BRIGHT + Fore.GREEN + "\tCliente Cadastrado com sucesso!"

def validar_nome (nome):
    for j in nome:
        if j >= '0' and j <= '9':
         return False
    i = 0

    while i < len(nome):
       
       if nome[i] in "!@#$%¨&*()_,?/´`^~:;}{[]<>+=-|\\'\"":
            return False
       i +=1
    return True
            
def validar_cpf(cadastro_de_pessoa):
    cpf = CPF()
    if cpf.validate(cadastro_de_pessoa):
        return True
    else:
        return False


def main(): #onde tudo irá acontecer.
    inicio = ""

    agenda = {}

    while inicio != "n":
        inicio = inicio_do_menu_()

        if inicio == "s":
            submenu = 1
            while submenu != 5:
                submenu = submenu_principal()

                if submenu == 1:
                    clientes_submenu = 1
                    while clientes_submenu != 7:
                        clientes_submenu = submenu_clientes()
                        
                        if clientes_submenu == 1:
                            nome = input(Style.BRIGHT + Fore.WHITE + "\n\tDigite o nome do cliente: ")
                            cpf = input(Style.BRIGHT + Fore.WHITE + "\tDigite o CPF do cliente: ")
                            i = 0
                            espaco = True

                            while i < len(nome):
                                if nome[i] != " ":
                                    espaco = False
                            i += 1

                            if len(nome) == 0 or espaco == True:
                                print(Fore.RED + Style.BRIGHT + "\n\tERRO! O nome não pode estar em branco.")
                            else:
                               sucesso, msng = cadastrar_clientes_cadastro_de_pessoa_fisica(nome, cpf, agenda)
                               print(msng)
                            
                            
                        elif clientes_submenu == 2:
                            print()
                        elif clientes_submenu == 3:
                            print()
                        elif clientes_submenu == 4:
                            print()
                        elif clientes_submenu == 5:
                            print()
                        elif clientes_submenu == 6:
                            print()
                        elif clientes_submenu == 7:
                            print(Fore.YELLOW + "\tVoltando...")
                        else:
                            print(Style.BRIGHT + Fore.RED + "\tERRO! OPÇÃO INVÁLIDA")

                elif submenu == 2:
                    veiculos_submenu = 1
                    while veiculos_submenu != 7:
                        veiculos_submenu = submenu_veiculos()
                        if veiculos_submenu == 1:
                            print()
                        elif veiculos_submenu == 2:
                            print()
                        elif veiculos_submenu == 3:
                            print()
                        elif veiculos_submenu == 4:
                            print()
                        elif veiculos_submenu == 5:
                            print()
                        elif veiculos_submenu == 6:
                            print()
                        elif veiculos_submenu == 7:
                            print(Fore.YELLOW + "\tVoltando...")
                        else:
                            print(Style.BRIGHT + Fore.RED + "\tERRO! OPÇÃO INVÁLIDA")


                elif submenu == 3:
                    alugueis_submenu = 1
                    while alugueis_submenu != 7:
                        alugueis_submenu = submenu_alugueis()

                        if alugueis_submenu == 1:
                            print()
                        elif alugueis_submenu == 2:
                            print()
                        elif alugueis_submenu == 3:
                            print()
                        elif alugueis_submenu == 4:
                            print()
                        elif alugueis_submenu == 5:
                            print()
                        elif alugueis_submenu == 6:
                            print()
                        elif alugueis_submenu == 7:
                            print(Fore.YELLOW + "\tVoltando...")
                        else:
                            print(Style.BRIGHT + Fore.RED + "\tERRO! OPÇÃO INVÁLIDA")
                        

                elif submenu == 4:
                    relatorio_submenu = 1
                    while relatorio_submenu != 4:
                        relatorio_submenu = submenu_relatorio()

                        if relatorio_submenu == 1:
                            print()
                        elif relatorio_submenu == 2:
                            print()
                        elif relatorio_submenu == 3:
                            print()
                        elif relatorio_submenu == 4:
                            print(Fore.YELLOW + "\tVoltando...")
                        else:
                            print(Style.BRIGHT + Fore.RED + "\tERRO! OPÇÃO INVÁLIDA")

                elif submenu == 5:
                    print(Style.BRIGHT + Fore.YELLOW + "\n\tEncerrando o Sistema...")
                    print(Fore.BLACK + Style.BRIGHT + "\tPrograma Encerrado.")
                else:
                    print(Fore.RED + "\n\tERRO! ESCOLHA UMA OPÇÃO VÁLIDA!")
        else:
            print(Style.BRIGHT + Fore.YELLOW + "\n\tEncerrando Programa...")
            print(Fore.BLACK + Style.BRIGHT + "\tPrograma Encerrado.")


main()