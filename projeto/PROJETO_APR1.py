
from colorama import init, Fore, Style #Biblioteca de cores
init(autoreset=True) #aqui ele reseta as cores a cada print automaticamente

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
        "Buscar Cliente por CPF",
        "Atualizar Cadastro",
        "Excluir Cliente",
        "Adicionar Telefone",
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

def verificar_cpf (cpf,dic_clientes): 
    vazio = True
    i = 0 
    while i <len(cpf):
        if cpf[i] != " ":
            vazio = False
        i += 1
    if vazio:
        return False
    
    i = 0
    while i<10:
        if cpf[i] < "0" or cpf[i] > "9":
            return False
        i += 1

    if cpf in dic_clientes:
        return False
    else:
        return True

def verificar_nome(nome):
    vazio = True
    i = 0
    while i < len(nome):
        if nome[i] != " ":
            vazio = False
        i += 1
    if vazio:
        return False

    i = 0
    while i < len(nome):
        letra = nome[i]
        if not ((letra >= "A" and letra <= "Z") or (letra >= "a" and letra <= "z") or letra == " "):
            return False
        i += 1
    return True

def verificar_data_de_nascimento_cliente(nascimento):
    if len(nascimento) != 10:
        return False
    
    if nascimento[2] != "/" or nascimento[5] != "/":
        return False

    i = 0
    while i < len(nascimento):
        if i != 2 and i != 5: 
            if nascimento[i] < "0" or nascimento[i] > "9":
                return False
        i += 1

    return True

def verificar_endereco(endereco):
    #está verificando se o endereço não está totalmente  vazio
    vazio = True
    i = 0
    while i < len(endereco):
        if endereco[i] != " ":
            vazio = False
        i += 1

    if vazio:
        return False
    
    #aqui ele esta verificando se tem pelo menos uma letra ou numero no endereço
    tem_caractere_valido = False
    i = 0
    while i < len(endereco):
        letra = endereco[i]
        if (letra >= "A" and letra <= "Z") or (letra >= "a" and letra <= "z") or (letra >= "0" and letra <= "9"):
            tem_caractere_valido = True
        i += 1

    if tem_caractere_valido == False:
        return False

    return True


def imprimir_cliente_formatado(cpf, dicionario_clientes):
    cliente = dicionario_clientes[cpf]

    print(Fore.CYAN + "\n\tDados cadastrados:")
    print(Fore.WHITE + "\tNome: " + cliente["Nome"])
    print(Fore.WHITE + "\tCPF: " + cpf)
    print(Fore.WHITE + "\tData de Nascimento: " + cliente["Data de Nascimento"])
    print(Fore.WHITE + "\tEndereço: " + cliente["Endereco"])

    if cliente["Telefone Fixo"] != []:  #se não estiver vazia
        print(Fore.WHITE + "\tTelefone Fixo: " + cliente["Telefone Fixo"][0])
    else:
        print(Fore.WHITE + "\tTelefone Fixo: (nenhum cadastrado)")

    if cliente["Telefone Celular"] != []:  #se não estiver vazia
        print(Fore.WHITE + "\tTelefone Celular: " + cliente["Telefone Celular"][0])
    else:
        print(Fore.WHITE + "\tTelefone Celular: (nenhum cadastrado)")


def excluir_telefone(cpf, dic_clientes, tipo_telefone, telefone):
    if tipo_telefone == "fixo":
        telefone_key = "Telefone Fixo"
    elif tipo_telefone == "celular":
        telefone_key = "Telefone Celular"
    else:
        return Style.BRIGHT + Fore.RED + "\tERRO! Tipo de telefone inválido."

    if telefone_key in dic_clientes[cpf]:
        if telefone in dic_clientes[cpf][telefone_key]:
            dic_clientes[cpf][telefone_key].remove(telefone)
            return Style.BRIGHT + Fore.GREEN + "\tTelefone excluído com sucesso!"
        else:
            return Style.BRIGHT + Fore.RED + "\tERRO! Número de telefone não encontrado."
    else:
        return Style.BRIGHT + Fore.RED + "\tERRO! Tipo de telefone não cadastrado para este cliente."

def buscar_cliente_por_cpf(cpf, dic_clientes):
    if cpf in dic_clientes:
        for i in dic_clientes[cpf]:
            print(f"\t{i}: {dic_clientes[cpf][i]}")
        return True 
    else:
        return False

def adicionar_telefone(cpf, dic_clientes, tipo_telefone, telefone):
    if tipo_telefone == "fixo":
        return adicionar_telefone_fixo(cpf, dic_clientes, telefone)
    elif tipo_telefone == "celular":
        return adicionar_telefone_celular(cpf, dic_clientes, telefone)
    else:
        return Style.BRIGHT + Fore.RED + "\tERRO! Tipo de telefone inválido."    


def adicionar_telefone_fixo(cpf, dic_clientes, telefone_fixo):
    if "Telefone Fixo" not in dic_clientes[cpf]:
        dic_clientes[cpf]["Telefone Fixo"] = []

    
    if telefone_fixo in dic_clientes[cpf]["Telefone Fixo"]:
        return Style.BRIGHT + Fore.RED + "\tERRO! Número já adicionado."
    else:
        dic_clientes[cpf]["Telefone Fixo"].append(telefone_fixo)
        return Style.BRIGHT + Fore.GREEN + "\tTelefone cadastrado com sucesso!"
    
def adicionar_telefone_celular(cpf, dic_clientes, telefone_celular):
    if "Telefone Celular" not in dic_clientes[cpf]:
        dic_clientes[cpf]["Telefone Celular"] = []

    
    if telefone_celular in dic_clientes[cpf]["Telefone Celular"]:
        return Style.BRIGHT + Fore.RED + "\tERRO! Número já adicionado."
    else:
        dic_clientes[cpf]["Telefone Celular"].append(telefone_celular)
        return Style.BRIGHT + Fore.GREEN + "\tTelefone cadastrado com sucesso!"
    
def atualizar_cadastro(cpf, dic_clientes, campo, novo_valor):
    if cpf in dic_clientes:
        if campo in dic_clientes[cpf]:
            dic_clientes[cpf][campo] = novo_valor
            return Style.BRIGHT + Fore.GREEN + "\tCadastro atualizado com sucesso!"
        else:
            return Style.BRIGHT + Fore.RED + "\tERRO! Campo inválido."
    else:
        return Style.BRIGHT + Fore.RED + "\tERRO! Cliente não encontrado."
    
def excluir_cliente(cpf, dic_clientes):
    if cpf in dic_clientes:
        del dic_clientes[cpf]
        return Style.BRIGHT + Fore.GREEN + "\tCliente excluído com sucesso!"
    else:
        return Style.BRIGHT + Fore.RED + "\tERRO! Cliente não encontrado."
    
def main(): #onde tudo irá acontecer
    inicio = ""

    dicionario_clientes = {}

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
                            # CADASTRO DE CLIENTE
                            cpf_ok = False
                            while cpf_ok == False:
                                cpf = input("\tDigite o CPF (só números): ")

                                vazio = True
                                i = 0
                                while i < len(cpf):
                                    if cpf[i] != " ":
                                        vazio = False
                                    i += 1

                                so_numeros = True
                                i = 0
                                while i < len(cpf):
                                    if cpf[i] < "0" or cpf[i] > "9":
                                        so_numeros = False
                                    i += 1

                                if vazio == False and so_numeros == True and cpf not in dicionario_clientes:
                                    cpf_ok = True
                                else:
                                    print(Fore.RED + "\tCPF inválido ou já cadastrado!")

                            # NOME
                            nome_ok = False
                            while nome_ok == False:
                                nome = input("\tDigite o Nome: ")
                                if verificar_nome(nome):
                                    nome_ok = True
                                else:
                                    print(Fore.RED + "\tNome inválido!")

                            #está validando a data de nascimento
                            data_ok = False
                            while data_ok == False:
                                nascimento = input("\tDigite a data de nascimento (DD/MM/AAAA): ")
                                if verificar_data_de_nascimento_cliente(nascimento):
                                    data_ok = True
                                else:
                                    print(Fore.RED + "\tData inválida!")

                            #está validando o endereço
                            end_ok = False
                            while end_ok == False:
                                endereco = input("\tDigite o endereço: ")
                                if verificar_endereco(endereco):
                                    end_ok = True
                                else:
                                    print(Fore.RED + "\tEndereço inválido!")

                            #está validando o telefone fixo
                            fixo_ok = False
                            while fixo_ok == False:
                                tel_fixo = input("\tDigite telefone fixo: ")
                                if tel_fixo != "" :
                                    fixo_ok = True
                                else:
                                    print(Fore.RED + "\tTelefone fixo inválido!")

                            #está validando o telefone celular
                            cel_ok = False
                            while cel_ok == False:
                                tel_cel = input("\tDigite telefone celular: ")
                                if tel_cel != "":
                                    cel_ok = True
                                else:
                                    print(Fore.RED + "\tTelefone celular inválido!")

                            #ele só cria e adiciona o cliente no dicionário aqui
                            dicionario_clientes[cpf] = {
                                "Nome": nome,
                                "Data de Nascimento": nascimento,
                                "Endereco": endereco,
                                "Telefone Fixo": [tel_fixo],
                                "Telefone Celular": [tel_cel]
                            }

                            print(Fore.GREEN + "\n\tCliente cadastrado com sucesso!")
                            imprimir_cliente_formatado(cpf, dicionario_clientes)

                        elif clientes_submenu == 2:
                            if len(dicionario_clientes) == 0:
                                print(Fore.RED + "\n\tNenhum cliente cadastrado!")
                            else:
                                buscar_cliente = input("\tDigite o CPF do cliente que deseja excluir o telefone: ")
                                if buscar_cliente in dicionario_clientes:
                                    imprimir_cliente_formatado(buscar_cliente, dicionario_clientes)

                                    tipo_telefone = ""
                                    while tipo_telefone not in ["fixo", "celular"]:
                                        tipo_telefone = input("\tDigite o tipo de telefone que deseja excluir (fixo/celular): ").lower()
                                        if tipo_telefone not in ["fixo", "celular"]:
                                            print(Fore.RED + "\tTipo inválido! Digite 'fixo' ou 'celular'.")

                                    telefone = input("\tDigite o número de telefone que deseja excluir: ")
                                    resultado = excluir_telefone(buscar_cliente, dicionario_clientes, tipo_telefone, telefone)
                                    print(resultado)
                                else:
                                    print(Fore.RED + "\n\tCliente não encontrado!")
                            
                        elif clientes_submenu == 3:
                            if len(dicionario_clientes) == 0:
                                print(Fore.RED + "\n\tNenhum cliente cadastrado!")
                            else:
                                buscar_cliente = input("\tDigite o CPF do cliente que deseja buscar: ")
                                if buscar_cliente in dicionario_clientes:
                                    imprimir_cliente_formatado(buscar_cliente, dicionario_clientes)
                                else:
                                    print(Fore.RED + "\n\tCliente não encontrado!")
                        elif clientes_submenu == 4:
                            if len(dicionario_clientes) == 0:
                                print(Fore.RED + "\n\tNenhum cliente cadastrado!")
                            else:
                                buscar_cliente = input("\tDigite o CPF do cliente que deseja atualizar o cadastro: ")
                                if buscar_cliente in dicionario_clientes:
                                    imprimir_cliente_formatado(buscar_cliente, dicionario_clientes)

                                    print(Fore.CYAN + "\n\tCampos disponíveis para atualização:")
                                    print(Fore.CYAN + "\t1. Nome")
                                    print(Fore.CYAN + "\t2. Data de Nascimento")
                                    print(Fore.CYAN + "\t3. Endereço")

                                    campo_opcao = ""
                                    while campo_opcao not in ["1", "2", "3"]:
                                        campo_opcao = input("\tDigite o número do campo que deseja atualizar: ")
                                        if campo_opcao not in ["1", "2", "3"]:
                                            print(Fore.RED + "\tOpção inválida! Digite 1, 2 ou 3.")

                                    if campo_opcao == "1":
                                        novo_valor = input("\tDigite o novo Nome: ")
                                        campo = "Nome"
                                    elif campo_opcao == "2":
                                        novo_valor = input("\tDigite a nova Data de Nascimento (DD/MM/AAAA): ")
                                        campo = "Data de Nascimento"
                                    elif campo_opcao == "3":
                                        novo_valor = input("\tDigite o novo Endereço: ")
                                        campo = "Endereco"

                                    resultado = atualizar_cadastro(buscar_cliente, dicionario_clientes, campo, novo_valor)
                                    print(resultado)
                                else:
                                    print(Fore.RED + "\n\tCliente não encontrado!")
                        elif clientes_submenu == 5: 
                            if len(dicionario_clientes) == 0:
                                print(Fore.RED + "\n\tNenhum cliente cadastrado!")
                            else:
                                buscar_cliente = input("\tDigite o CPF do cliente que deseja excluir: ")
                                if buscar_cliente in dicionario_clientes:
                                    imprimir_cliente_formatado(buscar_cliente, dicionario_clientes)
                                    confirmacao = input("\tTem certeza que deseja excluir este cliente? (s/n): ").lower()
                                    if confirmacao == "s":
                                        resultado = excluir_cliente(buscar_cliente, dicionario_clientes)
                                        print(resultado)
                                    else:
                                        print(Fore.YELLOW + "\n\tExclusão cancelada.")
                                else:
                                    print(Fore.RED + "\n\tCliente não encontrado!")
                        elif clientes_submenu == 6:
                            if len(dicionario_clientes) == 0:
                                print(Fore.RED + "\n\tNenhum cliente cadastrado!")
                            else:
                                buscar_cliente = input("\tDigite o CPF do cliente que deseja adicionar o telefone: ")
                                if buscar_cliente in dicionario_clientes:
                                    imprimir_cliente_formatado(buscar_cliente, dicionario_clientes)
                                    tipo_telefone = ""
                                    while tipo_telefone not in ["fixo", "celular"]:
                                        tipo_telefone = input("\tDigite o tipo de telefone que deseja adicionar (fixo/celular): ").lower()
                                        if tipo_telefone not in ["fixo", "celular"]:
                                            print(Fore.RED + "\tTipo inválido! Digite 'fixo' ou 'celular'.")

                                    telefone = input("\tDigite o número de telefone que deseja adicionar: ")
                                    resultado = adicionar_telefone(buscar_cliente, dicionario_clientes, tipo_telefone, telefone)
                                    print(resultado)
                                else:
                                    print(Fore.RED + "\n\tCliente não encontrado!")
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