
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


def exibir_submenu(titulo, cor, opcoes): #função genérica para os submenus, contendo as linhas em volta do título, cor e o titulo, ele também vai enquadrar o titulo no meio do retângulo.
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

def submenu_relatorio():
    return exibir_submenu("SUBMENU DE RELATÓRIOS", Fore.BLUE, [
        "Relatório: Reservas por CPF",
        "Relatório: Reservas por Código do Veículo",
        "Relatório: Reservas por Período",
        "Voltar"
    ])



# ---------FUNÇÕES DAS OPÇÕES DO SUBMENU CLIENTES---------

def verificar_cpf (cpf,dic_clientes): #verificação do cpf para ver se não está vazio ou se não tem letras no lugar de números
    vazio = True
    i = 0 
    while i <len(cpf): 
        if cpf[i] != " ": #se o cpf na posição i for diferente que espaço, ele vai transformar o vazio em falso e se o vazio for verdadeiro, retorna falso.
            vazio = False
        i += 1
    if vazio: #se estiver vazio, vai retornar falso
        return False
    
    i = 0
    while i<10: #verificando se tem somente números nos 10 primeiros caracteres
        if cpf[i] < "0" or cpf[i] > "9":
            return False
        i += 1

    if cpf in dic_clientes: #se o cpf já estiver adicionado no dicioário ele vai retornar falso
        return False
    else:
        return True

def verificar_nome(nome): #verificação do nome
    vazio = True
    i = 0

    while i < len(nome): #verificando se o nome não teem só espaço ou se está vazio
        if nome[i] != " ":
            vazio = False
        i += 1

    if vazio:
        return False
    
    i = 0
    while i < len(nome): #verificando se o nome na posição i não tem números.
        letra = nome[i]
        if not ((letra >= "A" and letra <= "Z") or (letra >= "a" and letra <= "z") or letra == " "):
            return False
        i += 1
    return True

def verificar_data_de_nascimento_cliente(nascimento): #verificação da data de nascimento
    if len(nascimento) != 10: #a quantidade de caracteres do nascimento tem que ser 10, se não for vai retornar falso.
        return False
    
    if nascimento[2] != "/" or nascimento[5] != "/": #se no index 2 não estiver / ou no index 5 não estiver / retorna falso.
        return False

    i = 0
    while i < len(nascimento):
        if i != 2 and i != 5: #se a posição não for 2 ou não for 5 ele passa para a proxima verificação, porque nessas posições estão a /
            if nascimento[i] < "0" or nascimento[i] > "9": # se for menor que 0 ou maior que 9 retorna falso
                return False
        i += 1

    return True

def verificar_endereco(endereco):
    #está verificando se o endereço não está totalmente  vazio
    vazio = True
    i = 0
    while i < len(endereco): #enquanto o tamanho do endereço de valor i fora diferente que espaço, o vazio que é verdadeiro retorna falso.
        if endereco[i] != " ":
            vazio = False
        i += 1

    if vazio: #se estiver totalmente vazio ele vai retornar falso.
        return False
    
    tem_letra = False #como o endereço precisa ter número e letra, criei duas variaveis para fazer essa verificação
    tem_numero = False
    i = 0

    while i < len(endereco):
        if (endereco[i] >= "A" and endereco[i] <= "Z") or (endereco[i] >= "a" and endereco[i] <= "z"):
            tem_letra = True

        if endereco[i] >= "0" and endereco[i] <= "9":
            tem_numero = True

        i += 1

    if not tem_letra or not tem_numero: #se não tiver letra e número retorna falso.
        return False
    return True

def imprimir_cliente_formatado(cpf, dicionario_clientes): #funçao para imprimir os dados do cliente
    cliente = dicionario_clientes[cpf]  # pega dentro do dicionário o cliente que tem esse CPF

    print(Fore.CYAN + "\n\tDados cadastrados:")
    print(Fore.WHITE + "\tNome: " + cliente["Nome"])  # imprime o valor da chave "Nome" do dicionário do cliente
    print(Fore.WHITE + "\tCPF: " + cpf) #está imprimindo o cpf que foi passado como parâmetro 
    print(Fore.WHITE + "\tData de Nascimento: " + cliente["Data de Nascimento"])
    print(Fore.WHITE + "\tEndereço: " + cliente["Endereco"]) # imprime o endereço que está salvo no dicionário do cliente

    if cliente["Telefone Fixo"]  != []:  #se não tiver vazia vai printar o primeiro número cadastrado.
        print(Fore.WHITE + "\tTelefone Fixo: " + cliente["Telefone Fixo"][0])
    else:
        print(Fore.WHITE + "\tTelefone Fixo: (nenhum cadastrado)") #Essa mensagem vai ser impressa caso o usuário excluir o telefone fixo e imprimir o relatório do cliente x.

    if cliente["Telefone Celular"] != []:
        print(Fore.WHITE + "\tTelefone Celular: " + cliente["Telefone Celular"][0])
    else:
        print(Fore.WHITE + "\tTelefone Celular: (nenhum cadastrado)")


def excluir_telefone(cpf, dic_clientes, tipo_telefone, telefone):
    #função recebe o cpf do cliente, o dicionário, o tipo de telefone e o número que será excluído.

    if tipo_telefone == "fixo": # está definindo qual chave será usada no dicionário
        telefone_key = "Telefone Fixo"
    elif tipo_telefone == "celular":
        telefone_key = "Telefone Celular"
    else:
        # Se o usuário digitar algo diferente de "fixo" ou "celular"
        return Style.BRIGHT + Fore.RED + "\tERRO! Tipo de telefone inválido."
    
    if telefone_key in dic_clientes[cpf]:  #verifica se o cliente possui esse tipo de telefone cadastrado

        # Verifica se o número realmente está na lista daquele tipo
        if telefone in dic_clientes[cpf][telefone_key]:
            
            dic_clientes[cpf][telefone_key].remove(telefone)#remove o número da lista

            return Style.BRIGHT + Fore.GREEN + "\tTelefone excluído com sucesso!"

        else:
            return Style.BRIGHT + Fore.RED + "\tERRO! Número de telefone não encontrado."
    
    else:
        #caso o cliente não conter telefone desse tipo
        return Style.BRIGHT + Fore.RED + "\tERRO! Tipo de telefone não cadastrado para este cliente."


def buscar_cliente_por_cpf(cpf, dic_clientes): #buscando o cpf do cliente que recebe como parâmetro o cpf e dicionário.
    if cpf in dic_clientes:  #verifica se o CPF existe no dicionário
        for i in dic_clientes[cpf]: # percorre cada chave do cliente
            print(f"\t{i}: {dic_clientes[cpf][i]}")# imprime a chave e o valor correspondente variàvel i 
        return True 
    else:
        return False

def adicionar_telefone(cpf, dic_clientes, tipo_telefone, telefone): #função que verifica
    
    if tipo_telefone == "fixo":    
        #verifica se o telefone contém apenas números
        i = 0
        while i < len(telefone):
            if telefone[i] < "0" or telefone[i] > "9":  # se não for número
                return Style.BRIGHT + Fore.RED + "\tERRO! O telefone deve conter apenas números."
            i += 1

        #se deu tudo certo manda para a função "adicionar_telefone_fixo"
        return adicionar_telefone_fixo(cpf, dic_clientes, telefone)

    elif tipo_telefone == "celular":
        i = 0
        while i < len(telefone):
            if telefone[i] < "0" or telefone[i] > "9":
                return Style.BRIGHT + Fore.RED + "\tERRO! O telefone deve conter apenas números."
            i += 1
        
        return adicionar_telefone_celular(cpf, dic_clientes, telefone)

    else:
        return Style.BRIGHT + Fore.RED + "\tERRO! Tipo de telefone inválido."


def adicionar_telefone_fixo(cpf, dic_clientes, telefone_fixo):
    if "Telefone Fixo" not in dic_clientes[cpf]:
        dic_clientes[cpf]["Telefone Fixo"] = []

    
    if telefone_fixo in dic_clientes[cpf]["Telefone Fixo"]: #se o telefone fixo já estiver nas informações daquele cliente retorna uma mensagem de erro
        return Style.BRIGHT + Fore.RED + "\tERRO! Número já adicionado."
    else:
        dic_clientes[cpf]["Telefone Fixo"].append(telefone_fixo) # adiciona o telefone dentro da lista "Telefone Fixo" desse cliente
        return Style.BRIGHT + Fore.GREEN + "\tTelefone cadastrado com sucesso!"
    
def adicionar_telefone_celular(cpf, dic_clientes, telefone_celular): #função que realmente adiciona o número celular no cadastro do cliente
    if "Telefone Celular" not in dic_clientes[cpf]: #se o cliente ainda não tem a lista "Telefone Celular", cria uma lista vazia
        dic_clientes[cpf]["Telefone Celular"] = []

    
    if telefone_celular in dic_clientes[cpf]["Telefone Celular"]:
        return Style.BRIGHT + Fore.RED + "\tERRO! Número já adicionado."
    else:
        dic_clientes[cpf]["Telefone Celular"].append(telefone_celular)
        return Style.BRIGHT + Fore.GREEN + "\tTelefone cadastrado com sucesso!"
    
def atualizar_cadastro(cpf, dic_clientes, campo, novo_valor): #função que atualiza o cadastro do cliente
    if cpf in dic_clientes: #verifica se o cliente existe no dicionário
        if campo in dic_clientes[cpf]:  #verifica se a chave informada (ex: Nome, Endereco...) existe no cadastro do cliente
            dic_clientes[cpf][campo] = novo_valor  #atualiza o valor do campo com o novo valor informado
            return Style.BRIGHT + Fore.GREEN + "\tCadastro atualizado com sucesso!"
        else:
            return Style.BRIGHT + Fore.RED + "\tERRO! Campo inválido."
    else:
        return Style.BRIGHT + Fore.RED + "\tERRO! Cliente não encontrado." #se o cpf não existir no dicionário de clientes
    
def excluir_cliente(cpf, dic_clientes): #função que excluir  o cadastro do cliente
    if cpf in dic_clientes: #se o cpf estiver no dicionário, deleta.
        del dic_clientes[cpf]
        return Style.BRIGHT + Fore.GREEN + "\tCliente excluído com sucesso!"
    else:
        return Style.BRIGHT + Fore.RED + "\tERRO! Cliente não encontrado."
    
def inicializar_arquivo_clientes():
    try:
        # cria o arquivo se ele não existir
        open("clientes.txt", "x").close()
    except FileExistsError:
        pass  # se já existir, não faz nada

def carregar_clientes():
    clientes = {}
    try:
        with open("clientes.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha == "":
                    continue  # ignora linhas vazias

                # separa os campos do cliente
                campos = linha.split(";")
                cpf = campos[0]

                clientes[cpf] = {
                    "Nome": campos[1],
                    "Data de Nascimento": campos[2],
                    "Endereco": campos[3],
                    "Telefone Fixo": [campos[4]],
                    "Telefone Celular": [campos[5]]
                }
    except FileNotFoundError:
        pass

    return clientes

def salvar_cliente_arquivo(cpf, cliente_dict):
    with open("clientes.txt", "a", encoding="utf-8") as arquivo:
        linha = (
            f"{cpf};"
            f"{cliente_dict['Nome']};"
            f"{cliente_dict['Data de Nascimento']};"
            f"{cliente_dict['Endereco']};"
            f"{cliente_dict['Telefone Fixo'][0]};"
            f"{cliente_dict['Telefone Celular'][0]}\n"
        )
        arquivo.write(linha)

def remover_cliente_arquivo(cpf_remover):
    with open("clientes.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    with open("clientes.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            if not linha.startswith(cpf_remover + ";"):
                arquivo.write(linha)

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

def verificar_aluguel(cpf, Agendamentos):
    for aluguel in Agendamentos:
        if Agendamentos[aluguel]['CPF Cliente'] == cpf:
            return True
    return False

def carros_disponiveis(Carros, Agendamentos):
    print(Style.BRIGHT + Fore.CYAN + "\n\tCarros disponíveis para aluguel:")
    cont_Alugados = 0
    for codigo in Carros:
        alugado = False
        for agendamentos in Agendamentos:
            if Agendamentos[agendamentos]['Codigo Veículo'] == codigo:
                alugado = True
                break
        if not alugado:
            print(Style.BRIGHT + Fore.WHITE + f"\tCódigo: {codigo}")
            print(Style.BRIGHT + Fore.GREEN + f"\t Status: Disponível para aluguel\n")
        else:
            cont_Alugados += 1
            print(Style.BRIGHT + Fore.WHITE + f"\tCódigo: {codigo}")
            print(Style.BRIGHT + Fore.RED + f"\t Status: Indisponível para aluguel\n")
        
    if cont_Alugados == len(Carros):
        print(Style.BRIGHT + Fore.RED + "\tNenhum carro disponível para aluguel no momento.")

def remover_aluguel(codigo_aluguel_remover, Agendamentos, Agendamentos_Desativados):
    if codigo_aluguel_remover not in Agendamentos:
        return Style.BRIGHT + Fore.RED + "\tCódigo de aluguel não encontrado."
    else:
        try:
            print(Style.BRIGHT + Fore.YELLOW + f"\n\tInformações do aluguel com o código {codigo_aluguel_remover} a ser removido:")
            for mostrar_Informacao in Agendamentos[codigo_aluguel_remover]:
                print(Style.BRIGHT + Fore.WHITE + f"\t{mostrar_Informacao.capitalize()}: {Agendamentos[codigo_aluguel_remover][mostrar_Informacao]}")
                
            confirmar = input(Style.BRIGHT + Fore.WHITE + "\n\tO aluguel que está aparecendo, é esse mesmo a ser removido (s/n): ").lower()
            while confirmar not in 'sn':
                print(Style.BRIGHT + Fore.RED + "\n\tERRO! Digite apenas 's' ou 'n'.")
                confirmar = input(Style.BRIGHT + Fore.WHITE + "\tO aluguel que está aparecendo, é esse mesmo a ser removido (s/n): ").lower()

            if confirmar != 's':
                return Style.BRIGHT + Fore.YELLOW + "\tRemoção de aluguel cancelada pelo usuário."
            else:
                Agendamentos_Desativados[codigo_aluguel_remover] = Agendamentos[codigo_aluguel_remover]
                del Agendamentos[codigo_aluguel_remover]
                return Style.BRIGHT + Fore.GREEN + "\tAluguel removido com sucesso!"
        except ValueError:
            return Style.BRIGHT + Fore.RED + "\tAlgo de errado aconteceu. Tente novamente."
        
def buscar_aluguel_por_codigo(codigo_aluguel_buscar, Agendamentos):
    if codigo_aluguel_buscar not in Agendamentos:
        print(Style.BRIGHT + Fore.RED + "\tCódigo de aluguel não encontrado.")
    else:
        try:
            print(Style.BRIGHT + Fore.YELLOW + f"\n\tInformações do aluguel com o código {codigo_aluguel_buscar}:")
            for mostrar_Informacao in Agendamentos[codigo_aluguel_buscar]:
                print(Style.BRIGHT + Fore.WHITE + f"\t{mostrar_Informacao.capitalize()}: {Agendamentos[codigo_aluguel_buscar][mostrar_Informacao]}")
        except ValueError:
            print(Style.BRIGHT + Fore.RED + "\tAlgo de errado aconteceu. Tente novamente.")


def atualizar_aluguel(codigo_aluguel_atualizar, Agendamentos): #função para atualizar o aluguel
    if codigo_aluguel_atualizar not in Agendamentos: #verificando se o código do aluguel existe no dicionário
        return Style.BRIGHT + Fore.RED + "\tCódigo de aluguel não encontrado."
    
    try:
        print(Style.BRIGHT + Fore.YELLOW + f"\n\tInformações do aluguel com o código {codigo_aluguel_atualizar} a ser atualizado:")
        for mostrar_Informacao in Agendamentos[codigo_aluguel_atualizar]: #percorrendo as chaves do dicionário do aluguel
            print(Style.BRIGHT + Fore.WHITE + 
                  f"\t{mostrar_Informacao.capitalize()}: {Agendamentos[codigo_aluguel_atualizar][mostrar_Informacao]}") #imprime as informações do aluguel
        
        print(Style.BRIGHT + Fore.CYAN + "\n\tDigite os novos dados do aluguel (deixe em branco para manter o valor atual):")

        data_inicio = input(Style.BRIGHT + Fore.WHITE + "\tNova Data de Início (DD/MM/AAAA): ")
        data_fim = input(Style.BRIGHT + Fore.WHITE + "\tNova Data de Fim (DD/MM/AAAA): ")

        #continua a mesma coisa se o usuário deixar em branco
        if data_inicio.strip() == "":
            data_inicio = Agendamentos[codigo_aluguel_atualizar]["Data Início"]
        if data_fim.strip() == "":
            data_fim = Agendamentos[codigo_aluguel_atualizar]["Data Fim"]

        #validação 
        if not validar_data_aluguel(data_inicio, data_fim, Agendamentos):
            return Style.BRIGHT + Fore.RED + "\tDatas inválidas. Atualização cancelada."

        #Atualizando as datas no dicionário
        Agendamentos[codigo_aluguel_atualizar]["Data Início"] = data_inicio
        Agendamentos[codigo_aluguel_atualizar]["Data Fim"] = data_fim

        return Style.BRIGHT + Fore.GREEN + "\tAluguel atualizado com sucesso!"

    except Exception:
        return Style.BRIGHT + Fore.RED + "\tAlgo de errado aconteceu. Tente novamente."

# ---------FUNÇÕES PARA LISTAR OS ALUGUEIS---------
        
def listar_alugueis(Agendamentos): #função para listar os aluguéis ativos
    if len(Agendamentos) == 0: #se o dicionário estiver vazio
        print(Style.BRIGHT + Fore.RED + "\n\tNenhum aluguel registrado no momento.")
    else:
        print(Style.BRIGHT + Fore.CYAN + "\n\tLista de aluguéis registrados:") #se não estiver vazio imprime as informações
        for codigo in Agendamentos: #percorrendo os códigos dos aluguéis
            print(Style.BRIGHT + Fore.WHITE + f"\n\tCódigo do Aluguel: {codigo}")
            for mostrar_Informacao in Agendamentos[codigo]:
                print(Style.BRIGHT + Fore.WHITE + f"\t{mostrar_Informacao.capitalize()}: {Agendamentos[codigo][mostrar_Informacao]}")

def listar_historico_alugueis(Agendamentos_Desativados): #função para listar os aluguéis desativados
    if len(Agendamentos_Desativados) == 0: #se o dicionário estiver vazio
        print(Style.BRIGHT + Fore.RED + "\n\tNenhum aluguel desativado no momento.")
    else:
        print(Style.BRIGHT + Fore.CYAN + "\n\tLista de aluguéis desativados:")
        for codigo in Agendamentos_Desativados:
            print(Style.BRIGHT + Fore.WHITE + f"\n\tCódigo do Aluguel: {codigo}") #imprimindo o código do aluguel desativado
            for mostrar_Informacao in Agendamentos_Desativados[codigo]:
                print(Style.BRIGHT + Fore.WHITE + f"\t{mostrar_Informacao.capitalize()}: {Agendamentos_Desativados[codigo][mostrar_Informacao]}")       

 #---------FUNÇÕES PARA GERAR RELATÓRIOS---------

def relatorio_reservas_periodo(Agendamentos, data_inicio, data_fim, dicionario_clientes):
    from datetime import datetime

    try:
        inicio = datetime.strptime(data_inicio, "%d/%m/%Y")
        fim = datetime.strptime(data_fim, "%d/%m/%Y")
    except:
        print(Fore.RED + "\tDatas inválidas.")
        return

    encontrou = False
    print(Style.BRIGHT + Fore.CYAN + f"\n\tReservas entre {data_inicio} e {data_fim}\n")

    for codigo in Agendamentos:
        data_aluguel = datetime.strptime(Agendamentos[codigo]["Data Início"], "%d/%m/%Y")

        if inicio <= data_aluguel <= fim:
            encontrou = True
            cpf = Agendamentos[codigo]["CPF Cliente"]
            nome = dicionario_clientes[cpf]["Nome"] if cpf in dicionario_clientes else "Nome não encontrado"

            print(Fore.WHITE + f"\tCódigo do Aluguel: {codigo}")
            print(f"\tCPF: {cpf}")
            print(f"\tNome: {nome}")
            for campo in Agendamentos[codigo]:
                print(f"\t{campo}: {Agendamentos[codigo][campo]}")
            print()

    if not encontrou:
        print(Fore.RED + "\tNenhuma reserva encontrada no período.")


def relatorio_reservas_por_veiculo(Agendamentos, codigo_veiculo):
    encontrou = False
    print(Style.BRIGHT + Fore.CYAN + f"\n\tReservas do Veículo {codigo_veiculo}\n")

    for codigo in Agendamentos:
        if Agendamentos[codigo]["Codigo Veículo"] == codigo_veiculo:
            encontrou = True
            print(Fore.WHITE + f"\tCódigo do Aluguel: {codigo}")
            for campo in Agendamentos[codigo]:
                print(f"\t{campo}: {Agendamentos[codigo][campo]}")
            print()

    if not encontrou:
        print(Fore.RED + "\tNenhuma reserva encontrada para este veículo.")


def relatorio_reservas_por_cpf(Agendamentos, cpf):
    encontrou = False
    print(Style.BRIGHT + Fore.CYAN + f"\n\tReservas do CPF: {cpf}\n")

    for codigo in Agendamentos:
        if Agendamentos[codigo]["CPF Cliente"] == cpf:
            encontrou = True
            print(Fore.WHITE + f"\tCódigo: {codigo}")
            for campo in Agendamentos[codigo]:
                print(f"\t{campo}: {Agendamentos[codigo][campo]}")
            print()

    if not encontrou:
        print(Fore.RED + "\tNenhuma reserva encontrada para este CPF.")

def relatorio_alugueis(Agendamentos):
    caminho = "Relatorio_Alugueis.txt"
    arq = open(caminho,"w",encoding="utf-8")
    if exiteArquivo(caminho):
        for chave in Agendamentos:
            arq.write(f"Código do Aluguel: {chave};\n")
            for conteudo in Agendamentos[chave]:
                arq.write(f"{conteudo.capitalize()}: {Agendamentos[chave][conteudo]};\n")
            arq.write("\n")
        arq.close()
        return True
    
def relatorio_veeiculos(Carros):
    caminho = "Relatorio_Veiculos.txt"
    arq = open(caminho,"w",encoding="utf-8")
    if exiteArquivo(caminho):
        for chave in Carros:
            arq.write(f"Código: {chave};\n")
            for conteudo in Carros[chave]:
                arq.write(f"{conteudo.capitalize()}: {Carros[chave][conteudo]};\n")
            arq.write("\n")
        arq.close()
        return True
    
def relatorio_clientes(dicionario_clientes):
    caminho = "Relatorio_Clientes.txt"
    arq = open(caminho,"w",encoding="utf-8")
    if exiteArquivo(caminho):
        for chave in dicionario_clientes:
            arq.write(f"CPF: {chave};\n")
            for conteudo in dicionario_clientes[chave]:
                arq.write(f"{conteudo}: {dicionario_clientes[chave][conteudo]};\n")
            arq.write("\n")
        arq.close()
        return True
    
def inicializar_arquivo_alugueis():
    try:
        open("alugueis.txt", "x").close()  # cria se não existir
    except FileExistsError:
        pass

def salvar_aluguel_arquivo(codigo, aluguel_dict):
    with open("alugueis.txt", "a", encoding="utf-8") as arq:
        linha = (
            f"{codigo};"
            f"{aluguel_dict['CPF Cliente']};"
            f"{aluguel_dict['Codigo Veículo']};"
            f"{aluguel_dict['Data Início']};"
            f"{aluguel_dict['Data Fim']}\n"
        )
        arq.write(linha)

def carregar_alugueis():
    alugueis = {}
    try:
        with open("alugueis.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha == "":
                    continue

                campos = linha.split(";")
                codigo = campos[0]

                alugueis[codigo] = {
                    "CPF Cliente": campos[1],
                    "Codigo Veículo": campos[2],
                    "Data Início": campos[3],
                    "Data Fim": campos[4]
                }
    except FileNotFoundError:
        pass

    return alugueis



def main(): #onde tudo irá acontecer
   inicio = ""
   
   dicionario_clientes = {} # dicionário para armazenar os clientes
   Carros = {} # dicionário para armazenar os carros
   inicializar_arquivo_alugueis()
   Agendamentos = carregar_alugueis()
   Agendamentos_Desativados = {} # dicionário para armazenar os agendamentos desativados

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

                            salvar_cliente_arquivo(cpf, dicionario_clientes[cpf])


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
                                        remover_cliente_arquivo(buscar_cliente)
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
                            # Os veiculos que estão disponiveis
                            print(Style.BRIGHT + Fore.CYAN + "\n\tCarros disponíveis para aluguel:")
                            if len(Agendamentos) != 0:
                                for codigo in Carros:
                                    for aluguel in Agendamentos:
                                        if Agendamentos[aluguel]['Codigo Veículo'] != codigo or len(Agendamentos) == 0:
                                            print(Style.BRIGHT + Fore.WHITE + f"\n\tCódigo: {codigo}")
                                            for conteudo in Carros[codigo]:
                                                print(Style.BRIGHT + Fore.WHITE + f"\t{conteudo.capitalize()}: {Carros[codigo][conteudo]}")
                                            print(Style.BRIGHT + Fore.GREEN + f"\t Status: Disponível para aluguel")
                            else:
                                for codigo in Carros:
                                    print(Style.BRIGHT + Fore.WHITE + f"\n\tCódigo: {codigo}")
                                    for conteudo in Carros[codigo]:
                                        print(Style.BRIGHT + Fore.WHITE + f"\t{conteudo.capitalize()}: {Carros[codigo][conteudo]}")
                                    print(Style.BRIGHT + Fore.GREEN + f"\t Status: Disponível para aluguel")
                        elif veiculos_submenu == 6:
                            # Os veiculos que estão alugados
                            if len(Agendamentos) != 0 or len(Carros) != len(Agendamentos):
                                for codigo in Carros:
                                    for aluguel in Agendamentos:
                                        if Agendamentos[aluguel]['Codigo Veículo'] == codigo:
                                            print(Style.BRIGHT + Fore.WHITE + f"\n\tCódigo: {codigo}")
                                            for conteudo in Carros[codigo]:
                                                print(Style.BRIGHT + Fore.WHITE + f"\t{conteudo.capitalize()}: {Carros[codigo][conteudo]}")
                                            print(Style.BRIGHT + Fore.RED + f"\t Status: Indisponível para aluguel")
                            else:
                                print(Style.BRIGHT + Fore.RED + "\n\tNenhum carro está alugado no momento.")
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
                        if alugueis_submenu == 1:
                            codigo_aluguel = "aluguel-" + str(len(Agendamentos)+1)
                            if Carros != {}:
                                if cont != len(Carros):
                                    testeCPF = False
                                    while not testeCPF:
                                        cpf_cliente = input(Style.BRIGHT + Fore.WHITE + "\n\tDigite o CPF do cliente: ")
                                        if cpf_cliente in dicionario_clientes:
                                            if not verificar_cpf (cpf_cliente,dicionario_clientes):
                                                imprimir_cliente_formatado(cpf_cliente,  dicionario_clientes)
                                                testeCPF = True
                                            else:
                                                print(Style.BRIGHT + Fore.RED + "\n\tCPF inválido ou não cadastrado. Tente novamente.\n")
                                                break
                                            
                                            cpf_alugado = verificar_aluguel(cpf_cliente, Agendamentos)
                                            if cpf_alugado:
                                                print(Style.BRIGHT + Fore.RED + "\n\tCliente já possui um aluguel ativo. Não é possível realizar um novo aluguel.\n")
                                            else:
                                                carros_disponiveis(Carros, Agendamentos)
                                                testeVeiculo = False
                                                while not testeVeiculo:
                                                    if len(Carros) != len(Agendamentos):
                                                        codigo_veiculo = input(Style.BRIGHT + Fore.WHITE + "\tDigite o código do veículo: ")
                                                        if validar_codigo(codigo_veiculo):
                                                            if codigo_veiculo not in Agendamentos:
                                                                testeVeiculo = True
                                                            else:
                                                                print(Style.BRIGHT + Fore.RED + "\n\tVeículo já está alugado. Tente novamente.\n")
                                                        else:
                                                            print(Style.BRIGHT + Fore.RED + "\n\tCódigo inválido. Tente novamente.\n")
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
                                                        "Codigo Veículo": codigo_veiculo,
                                                        "Data Início": data_inicio,
                                                        "Data Fim": data_fim
                                                        }
                                                        print(Style.BRIGHT + Fore.GREEN + "\tAluguel registrado com sucesso!")
                                                    else:
                                                        testeVeiculo = True
                                        else:
                                            print(Style.BRIGHT + Fore.RED + "\n\tCPF não cadastrado. Volte para o inicio e faça o seu cadastro.\n")
                                            testeCPF = True
                            else: 
                                print(Style.BRIGHT + Fore.RED + "\n\tNenhum veículo cadastrado para ser aluguel.\n")
                        elif alugueis_submenu == 2:
                            codigo_aluguel_remover = input(Style.BRIGHT + Fore.WHITE + "\n\tDigite o código do aluguel que deseja remover: ")
                            mensagem_remover_aluguel = remover_aluguel(codigo_aluguel_remover, Agendamentos, Agendamentos_Desativados)
                            print(mensagem_remover_aluguel)
                        elif alugueis_submenu == 3:
                            codigo_aluguel_buscar = input(Style.BRIGHT + Fore.WHITE + "\n\tDigite o código do aluguel que deseja buscar: ")
                            buscar_aluguel_por_codigo(codigo_aluguel_buscar, Agendamentos)
                        elif alugueis_submenu == 4:
                            codigo_aluguel_atualizar = input(Style.BRIGHT + Fore.WHITE + "\n\tDigite o código do aluguel que deseja atualizar: ")
                            mensagem_atualizar_aluguel = atualizar_aluguel(codigo_aluguel_atualizar, Agendamentos)
                            print(mensagem_atualizar_aluguel)
                        elif alugueis_submenu == 5:
                            listar_alugueis(Agendamentos)
                        elif alugueis_submenu == 6:
                            listar_historico_alugueis(Agendamentos_Desativados)
                        elif alugueis_submenu == 7:
                            print(Fore.YELLOW + "\tVoltando...")
                        else:
                            print(Style.BRIGHT + Fore.RED + "\tERRO! OPÇÃO INVÁLIDA")
                        

                elif submenu == 4:
                    relatorio_submenu = 1
                    while relatorio_submenu != 4:
                        relatorio_submenu = submenu_relatorio()

                        if relatorio_submenu == 1:
                            cpf = input("\tDigite o CPF: ")
                            relatorio_reservas_por_cpf(Agendamentos, cpf)

                        elif relatorio_submenu == 2:
                            cod = input("\tDigite o código do veículo: ")
                            relatorio_reservas_por_veiculo(Agendamentos, cod)

                        elif relatorio_submenu == 3:
                            di = input("\tData início (DD/MM/AAAA): ")
                            df = input("\tData fim (DD/MM/AAAA): ")
                            relatorio_reservas_periodo(Agendamentos, di, df, dicionario_clientes)
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