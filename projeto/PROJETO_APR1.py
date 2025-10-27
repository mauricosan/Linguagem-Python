from colorama import init, Fore, Style
init(autoreset=True)

def inicio_do_menu_():
    print(Fore.CYAN + Style.BRIGHT + "\n\t🏁 Bem-vindo(a) à Locadora — onde sua jornada começa!")
    
    while True:
        escolha_do_sistema = input(Fore.LIGHTMAGENTA_EX + "\tDeseja iniciar o sistema da locadora? (s/n): ").lower()
        if escolha_do_sistema in ["s", "n"]:
            return escolha_do_sistema
        else:
            print(Style.BRIGHT + Fore.RED + "\n\tERRO! Digite apenas 's' ou 'n'.")


def exibir_submenu(titulo, cor, opcoes):
    largura = len(titulo) + 12
    print(Style.BRIGHT + cor + "\n" + "\t" + "╔" + "═" * largura + "╗")
    print(Style.BRIGHT + cor + "\t║" + f"{titulo:^{largura}}" + "║")
    print(Style.BRIGHT + cor + "\t╚" + "═" * largura + "╝")


    cont = 1
    for opcao in opcoes:
        print(f"\t{cont}. {opcao}")
        cont += 1

    while True:
        try:
            escolha = int(input(Style.BRIGHT + Fore.BLACK + "\tEscolha uma opção: "))
            return escolha
        except ValueError:
            print(Style.BRIGHT + Fore.RED + "\n\tUse apenas números válidos!")


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

def main():
    inicio = ""
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
                            print()
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
            print(Fore.WHITE + Style.BRIGHT + "\tPrograma Encerrado.")


main()