
from colorama import init, Fore, Style #Biblioteca de cores
init(autoreset=True) #aqui ele reseta as cores a cada print automaticamente
from validate_docbr import CPF
import requests #Biblioteca para fazer requisições HTTP

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

# ---------FUNÇÕES DAS OPÇÕES DO SUBMENU VEICULOS--------- 
# Validando o código do veículo
def validar_codigo(codigo):
    try:
        codigo = int(codigo)
        if codigo < 1000 or codigo > 100000:
            return False
    
        return True
    except ValueError:
        return False

# Validando a descrição do veículo
def validar_descricao(descricao):

    for char in descricao:
        if char in "!@#$%¨&*()_?/´`^~:;}{[]<>+=-|\\'\"0123456789":
            return False
        
    if len(descricao) == 0 or descricao.isspace():
        return False
    
    return True

def validar_categoria(categoria):
    for char in categoria:
        if char in "@#$%¨&*()_?/´`^~:;}{[]<>+=-|\\'\"0123456789":
            return False
        
    if len(categoria) == 0 or categoria.isspace():
        return False
        
    if categoria not in ["A", "B", "C", "D", "E", "SUV", "PICKUP", "LUXO"]:
        return False
    return True

def validar_capacidade(capacidade):
    try:
        capacidade = int(capacidade)
        if capacidade < 1 or capacidade > 7:
            return False
        return True
    except ValueError: 
        return False

def validar_combustivel(combustivel):
    for char in combustivel:
        if char in "!@#$%¨&*()_?/´`^~:;}{[]<>+=-|\\'\"0123456789":
            return False
        
    if len(combustivel) == 0 or combustivel.isspace():
        return False
        
    if combustivel not in ["Gasolina", "Álcool", "Flex", "Elétrico"]:
        return False
    return True

def validar_ano(ano):
    try:
        ano = int(ano)
        if ano < 2016 or ano > 2026:
            return False
        return True
    except ValueError: 
        return False

def validar_modelo(modelo,nome):
    if (len(modelo) == 0 or modelo.isspace()) and (len(nome) == 0 or nome.isspace()):
        return False
    else:
        # Testando se o modelo: Fiat existe ou não na vida erral
        url_modelo = requests.get(f"https://parallelum.com.br/fipe/api/v1/carros/marcas").json()
        
        modelo_codigo = None
        for modelos in url_modelo:
            if modelos["nome"].lower() == modelo.lower():
                modelo_codigo = modelos["codigo"]
                break
        
        if modelo_codigo == None:
            return False
        
        #Testando se o nome do carro: Argo 1.0 Flex existe
        url_nome = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{modelo_codigo}/modelos"
        
        modeloNome = requests.get(url_nome).json()["modelos"]
        
        
        for nomes in modeloNome:
            if nome.lower() in nomes["nome"].lower():
                return True
    
        return False

# ---------FUNÇÕES DAS OPÇÕES DO SUBMENU VEICULOS---------
def remover_veiculos(codigo_remover, Carros):
    if codigo_remover not in Carros:
        return Style.BRIGHT + Fore.RED + "\tCódigo não encontrado."
    else:
        try:
            codigo = int(codigo_remover)
            print(Style.BRIGHT + Fore.YELLOW + f"\n\tInformações do veículo com o código {codigo} a ser removido:")
            for mostrar_Informacao in Carros[codigo_remover]:
                print(Style.BRIGHT + Fore.WHITE + f"\t{mostrar_Informacao.capitalize()}: {Carros[codigo_remover][mostrar_Informacao]}")
                
            confirmar = input(Style.BRIGHT + Fore.WHITE + "\n\tO veiculo que está aparecendo, é esse mesmo a ser removido (s/n): ").lower()
            while confirmar not in 'sn':
                print(Style.BRIGHT + Fore.RED + "\n\tERRO! Digite apenas 's' ou 'n'.")
                confirmar = input(Style.BRIGHT + Fore.WHITE + "\tO veiculo que está aparecendo, é esse mesmo a ser removido (s/n): ").lower()

            if confirmar != 's':
                return Style.BRIGHT + Fore.YELLOW + "\tRemoção cancelada pelo usuário."
            else:
                del Carros[codigo_remover]
                return Style.BRIGHT + Fore.GREEN + "\tVeículo removido com sucesso!"
        except ValueError:
            return Style.BRIGHT + Fore.RED + "\tCódigo inválido."
## ---------FUNÇÕES PARA BUSCAR O VEICULO VINCULADO AO CODIGO DISPONIBILIZADO---------
def buscar_veiculos_por_codigo(buscar_codigo, Carros):
    if buscar_codigo not in Carros:
        return Style.BRIGHT + Fore.RED + "\tCódigo não encontrado."
    else:
        try:
            codigo = int(buscar_codigo)
            print(Style.BRIGHT + Fore.YELLOW + f"\n\tInformações do veículo com o código {codigo}:")
            for mostrar_Informacao in Carros[buscar_codigo]:
                print(Style.BRIGHT + Fore.WHITE + f"\t{mostrar_Informacao.capitalize()}: {Carros[buscar_codigo][mostrar_Informacao]}")
        except ValueError:
            print(Style.BRIGHT + Fore.RED + "\tCódigo inválido.")

# ---------FUNÇÕES PARA ATUALIZAR DADOS DO VEICULO VINCULADO AO CODIGO INFORMADO---------
def atualizar_veiculos(codigo_atualizar, Carros):
    if codigo_atualizar not in Carros:
        return Style.BRIGHT + Fore.RED + "\tCódigo não encontrado."
    else:
        try:
            codigo = int(codigo_atualizar)
            print(Style.BRIGHT + Fore.YELLOW + f"\n\tInformações do veículo com o código {codigo} a ser atualizado:")
            for mostrar_Informacao in Carros[codigo_atualizar]:
                print(Style.BRIGHT + Fore.WHITE + f"\t{mostrar_Informacao.capitalize()}: {Carros[codigo_atualizar][mostrar_Informacao]}")
            print(Style.BRIGHT + Fore.CYAN + "\n\tDigite os novos dados do veículo (deixe em branco para manter o valor atual):")
                            
            #Validando a descrisão do veículo para inserir novamente
            descricao = input(Style.BRIGHT + Fore.WHITE + "\tDigite a descrição do veículo: ")
                            
            #Validando a categoria do veículo para inserir novamente
            categoria = input(Style.BRIGHT + Fore.WHITE + "\tDigite a categoria do veículo: ").upper()
                    
                            
            #Validando a capacidade do veículo colocado pelo usuário
            capacidade = input(Style.BRIGHT + Fore.WHITE + "\tDigite a capacidade do veículo: ")
                            
            #Validando o combustivel do veículo para inserir novamente
            combustivel = input(Style.BRIGHT + Fore.WHITE + "\tDigite o tipo de combustível do veículo (Gasolina, Álcool, Flex, Elétrico): ").capitalize()

            #Validando o ano do veiculo para inserir novamente
            ano = input(Style.BRIGHT + Fore.WHITE + "\tDigite o ano do veículo: ")
                    
            #Validando o modelo e nome do carro para inserir novamente
            modelo = input(Style.BRIGHT + Fore.WHITE + "\tDigite o modelo do veículo: ")
            nomeCarro = input(Style.BRIGHT + Fore.WHITE + "\tDigite o nome do carro: ")
            if descricao == "" or descricao.isspace():
                descricao = Carros[codigo_atualizar]["descricao"]
            if categoria == "" or categoria.isspace():
                categoria = Carros[codigo_atualizar]["categoria"]
            if capacidade == "" or capacidade.isspace():
                capacidade = Carros[codigo_atualizar]["capacidade"]
            if combustivel == "" or combustivel.isspace():
                combustivel = Carros[codigo_atualizar]["combustivel"]
            if ano == "" or ano.isspace():
                ano = Carros[codigo_atualizar]["ano"]
            if modelo == "" or modelo.isspace() or nomeCarro == "" or nomeCarro.isspace():
                modelo_nome_atual = Carros[codigo_atualizar]["modelo"].split(" ", 1)
                modelo = modelo_nome_atual[0]
                nomeCarro = modelo_nome_atual[1]
            
            Carros[codigo_atualizar]["descricao"] = descricao
            Carros[codigo_atualizar]["categoria"] = categoria
            Carros[codigo_atualizar]["capacidade"] = capacidade
            Carros[codigo_atualizar]["combustivel"] = combustivel
            Carros[codigo_atualizar]["ano"] = ano
            Carros[codigo_atualizar]["modelo"] = modelo + " " + nomeCarro
            return Style.BRIGHT + Fore.GREEN + "\tVeículo atualizado com sucesso!"
        except ValueError:
            return Style.BRIGHT + Fore.RED + "\tCódigo inválido."


##### Inserindo os dados do arquivo
def exiteArquivo(caminho):
    import os
    if os.path.exists(caminho):
        return True
    return False

def inserindoRelatorio(Carros):
    caminho = "Carros_Registrados.txt"
    arq = open(caminho,"w",encoding="utf-8")
    if exiteArquivo(caminho):
        for chave in Carros:
            arq.write(f"Código: {chave};\n")
            for conteudo in Carros[chave]:
                arq.write(f"{conteudo.capitalize()}: {Carros[chave][conteudo]};\n")
            arq.write("\n")
        arq.close()
        return True

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

############################## Parte do Aluguel de carros ##############################

def calendario():
    import calendar
    from datetime import datetime
    
    dia = datetime.now().day
    mes = datetime.now().month
    ano = datetime.now().year
    
    print(Style.BRIGHT + Fore.CYAN + "\nCalendário do mês atual:")
    print(Style.BRIGHT + Fore.WHITE + calendar.month(ano, mes))

def validar_data_aluguel(data_inicio, data_fim, Agendamentos):
    from datetime import datetime, timedelta # Importando timedelta para manipular datas
    try:
        inicio = datetime.strptime(data_inicio, "%d/%m/%Y") # Convertendo a string para objeto datetime
        fim = datetime.strptime(data_fim, "%d/%m/%Y") # Convertendo a string para objeto datetime
        
        if inicio >= fim: # Verificando se a data de início é antes da data de fim
            return False
        
        hoje = datetime.now() # Obtendo a data atual
        if inicio <= hoje or fim <= hoje: # Verificando se as datas são no passado ou no dia atual
            return False
        
        # Verificando se o período de aluguel não excede 30 dias
        if (fim - inicio).days > 30:
            return False
        
        # if (inicio - hoje).days < 1: # Verificando se a data de início é pelo menos 1 dia após a data atual
        #     return False
        
        return True
    except ValueError:
        return False
    
def main(): #onde tudo irá acontecer
    inicio = ""

    dicionario_clientes = {} # dicionário para armazenar os clientes
    Carros = {} # dicionário para armazenar os carros
    Agendamentos = {} # dicionário para armazenar os agendamentos

    


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
                            
                            #Validando o código do véiculo quando é inserido
                            validar = True
                            while validar:
                                codigo = input(Style.BRIGHT + Fore.WHITE + "\n\tDigite o código do veículo (1000 ate 100000): ")
                                if validar_codigo(codigo):
                                    if codigo in Carros:
                                        print(Style.BRIGHT + Fore.RED + "\n\tCódigo já cadastrado. Tente novamente.")
                                    else:
                                        validar = False
                                else:
                                    print(Style.BRIGHT + Fore.RED + "\n\tCódigo inválido. Tente novamente.\n")
                            
                            #Validando a descrisão do veículo colocado pele usuário
                            validar = True
                            while validar:
                                descricao = input(Style.BRIGHT + Fore.WHITE + "\tDigite a descrição do veículo: ")
                                if validar_descricao(descricao):
                                    validar = False
                                else:
                                    print(Style.BRIGHT + Fore.RED + "\n\tDescrição inválida. Tente novamente.\n")
                            
                            #Validando a categoria do veículo colocado pelo usuário
                            validar = True
                            while validar:
                                cat = input(Style.BRIGHT + Fore.WHITE + "\tDigite a categoria do veículo: ")
                                categoria = cat.upper()
                                if validar_categoria(categoria):
                                    validar = False
                                else:
                                    print(Style.BRIGHT + Fore.RED + "\n\tCategoria inválida. Tente novamente.\n")
                            
                            #Validando a capacidade do veículo colocado pelo usuário
                            validar = True
                            while validar:
                                capacidade = input(Style.BRIGHT + Fore.WHITE + "\tDigite a capacidade do veículo: ")
                                if validar_capacidade(capacidade):
                                    validar = False
                                else:
                                    print(Style.BRIGHT + Fore.RED + "\n\tCapacidade inválida. Tente novamente.\n")
                            
                            #Validando o combustivel do veículo colocado pelo usuário
                            validar = True
                            while validar:
                                combustivel = input(Style.BRIGHT + Fore.WHITE + "\tDigite o tipo de combustível do veículo (Gasolina, Álcool, Flex, Elétrico): ")
                                if validar_combustivel(combustivel):
                                    validar = False
                                else:
                                    print(Style.BRIGHT + Fore.RED + "\n\tCombustível inválido. Tente novamente.\n")
                            
                            #Validando o ano do veiculo colocando pelo usuário
                            validar = True
                            while validar:
                                ano = input(Style.BRIGHT + Fore.WHITE + "\tDigite o ano do veículo: ")
                                if validar_ano(ano):
                                    validar = False
                                else:
                                    print(Style.BRIGHT + Fore.RED + "\n\tAno inválido. Tente novamente.\n")
                            
                            #Validando o modelo e nome do carro colocado pelo usuário
                            validar = True
                            while validar:
                                modelo = input(Style.BRIGHT + Fore.WHITE + "\tDigite o modelo do veículo: ")
                                nomeCarro = input(Style.BRIGHT + Fore.WHITE + "\tDigite o nome do carro: ")
                                if validar_modelo(modelo,nomeCarro):
                                    validar = False
                                else:
                                    print(Style.BRIGHT + Fore.RED + "\n\tModelo ou nome do carro inválido. Tente novamente.\n")
                            
                            espaco = True
                            i = 0
                            
                            while i < len(codigo):
                                if codigo[i] != " ":
                                    espaco = False
                                i += 1
                            
                            if len(codigo) == 0 or espaco == True:
                                print(Fore.RED + Style.BRIGHT + "\n\tERRO! O código não pode estar em branco.")
                            else:
                                Carros[codigo] = {
                                    "descricao": descricao,
                                    "categoria": categoria,
                                    "capacidade": capacidade,
                                    "combustivel": combustivel,
                                    "ano": ano,
                                    "modelo": modelo + " " + nomeCarro
                                }
                                print(Style.BRIGHT + Fore.GREEN + "\tVeículo cadastrado com sucesso!")

                        elif veiculos_submenu == 2:
                            # Remover Veículos
                            codigo_remover = input(Style.BRIGHT + Fore.WHITE + "\n\tDigite o código do veículo que deseja remover: ")
                            mensagem_remover = remover_veiculos(codigo_remover, Carros)
                            print(mensagem_remover)
                        elif veiculos_submenu == 3:
                            # Buscar Veículos por Código
                            buscar_codigo = input(Style.BRIGHT + Fore.WHITE + "\n\tDigite o código do veículo que deseja buscar: ")
                            mensagem_buscar = buscar_veiculos_por_codigo(buscar_codigo, Carros)
                        elif veiculos_submenu == 4:
                            codigo_atualizar = input(Style.BRIGHT + Fore.WHITE + "\n\tDigite o código do veículo que deseja atualizar: ")
                            mensagem_atualizar = atualizar_veiculos(codigo_atualizar, Carros)
                            print(mensagem_atualizar)
                        elif veiculos_submenu == 5:
                            print()
                        elif veiculos_submenu == 6:
                            print()
                        elif veiculos_submenu == 7:
                            print(Fore.YELLOW + "\tInserindo os Dados no Relatorio.....")
                            if inserindoRelatorio(Carros):
                                print(Fore.GREEN + "\tInserido os dados com sucesso..")
                            print(Fore.YELLOW + "\tVoltando...")

                        else:
                            print(Style.BRIGHT + Fore.RED + "\tERRO! OPÇÃO INVÁLIDA")


                elif submenu == 3:
                    alugueis_submenu = 1
                    while alugueis_submenu != 7:
                        alugueis_submenu = submenu_alugueis()
                        cont = 0
                        contador = 0
                        if alugueis_submenu == 1:
                            contador += 1
                            codigo_aluguel = "aluguel-" + str(contador)
                            if Carros != {}:
                                if cont != len(Carros):
                                    testeCPF = False
                                    while not testeCPF:
                                        cpf_cliente = input(Style.BRIGHT + Fore.WHITE + "\n\tDigite o CPF do cliente: ")
                                        if cpf_cliente in dicionario_clientes:
                                            if not verificar_cpf (cpf_cliente,dicionario_clientes):
                                                imprimir_cliente_formatado(cpf_cliente, dicionario_clientes)
                                                testeCPF = True
                                            else:
                                                print(Style.BRIGHT + Fore.RED + "\n\tCPF inválido ou não cadastrado. Tente novamente.\n")
                    
                                        else:
                                            print(Style.BRIGHT + Fore.RED + "\n\tCPF não cadastrado. Volte para o inicio e faça o seu cadastro.\n")
                                            submenu_alugueis()
                                    
                                    # Verificando se o cpf do cliente já está vinculado a um aluguel
                                    cpf_alugado = False
                                    for cpf_aluguel in Agendamentos:
                                        for itens in Agendamentos[cpf_aluguel]:
                                            aluguel = Agendamentos[cpf_aluguel]
                                            if aluguel["CPF Cliente"] == cpf_cliente:
                                                cpf_alugado = True
                                                break
                                        
                                    if cpf_alugado:
                                        print(Style.BRIGHT + Fore.RED + "\n\tCliente já possui um aluguel ativo. Não é possível realizar um novo aluguel.\n")
                                        submenu_alugueis()
                                    # Mostrando os carros disponíveis para aluguel
                                    
                                    print(Style.BRIGHT + Fore.CYAN + "\n\tCarros disponíveis para aluguel:")
                                    
                                    for codigo, detalhes in Carros.items():
                                        
                                        print(Style.BRIGHT + Fore.WHITE + f"\n\tCódigo: {codigo}")
                                        
                                        #verificando se o veículo está alugado
                                        contAlugueis = 0
                                        alugado = False
                                        for aluguel in Agendamentos.values():
                                            if aluguel["Código Veículo"] == codigo:
                                                alugado = True
                                                break
                                        
                                        #se tiver alugado
                                        todosVeiculosAlugados = True
                                        if alugado:
                                            print(Style.BRIGHT + Fore.RED + "\tStatus: Alugado")
                                            contAlugueis = contAlugueis + 1
                                        else:
                                            print(Style.BRIGHT + Fore.GREEN + "\tStatus: Disponível")
                                            todosVeiculosAlugados = False
                                        
                                        if todosVeiculosAlugados and contAlugueis == len(Carros):
                                            print(Style.BRIGHT + Fore.RED + "\n\tNenhum veículo disponível para aluguel no momento.\n")
                                            submenu_alugueis()
                                                
                                    testeVeiculo = False
                                    while not testeVeiculo:
                                        codigo_veiculo = input(Style.BRIGHT + Fore.WHITE + "\tDigite o código do veículo: ")
                                        if validar_codigo(codigo_veiculo):
                                            if codigo_veiculo not in Agendamentos:
                                                testeVeiculo = True
                                            else:
                                                print(Style.BRIGHT + Fore.RED + "\n\tVeículo já está alugado. Tente novamente.\n")
                                        else:
                                                print(Style.BRIGHT + Fore.RED + "\n\tCódigo inválido. Tente novamente.\n")
                                else:
                                    print(Style.BRIGHT + Fore.RED + "\n\tNenhum veículo disponível para aluguel no momento.\n")
                                    submenu_alugueis()
                                
                                calendario()
                                verificar_datas = False
                                while not verificar_datas:
                                    data_inicio = input(Style.BRIGHT + Fore.WHITE + "\tDigite a data de início do aluguel (DD/MM/AAAA): ")
                                    data_fim = input(Style.BRIGHT + Fore.WHITE + "\tDigite a data de fim do aluguel (DD/MM/AAAA): ")
                                    if validar_data_aluguel(data_inicio, data_fim, Agendamentos):
                                        verificar_datas = True
                                    else:
                                        print(Style.BRIGHT + Fore.RED + "\n\tDatas inválidas ou periodo já alugado. Tente novamente.\n")
                                
                                Agendamentos[codigo_aluguel] = {
                                    "CPF Cliente": cpf_cliente,
                                    "Código Veículo": codigo_veiculo,
                                    "Data Início": data_inicio,
                                    "Data Fim": data_fim
                                }
                                print(Style.BRIGHT + Fore.GREEN + "\tAluguel registrado com sucesso!")
                            else: 
                                print(Style.BRIGHT + Fore.RED + "\n\tNenhum veículo cadastrado para ser aluguel.\n")
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

if __name__ == "__main__":
    main()