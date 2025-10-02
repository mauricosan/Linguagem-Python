# Uma Unidade de Pronto Atendimento precisa de uma aplicação para gerenciar a fila de
# atendimento dos pacientes que buscam ser atendidos pela UPA. Cada paciente que chega
# procurando atendimento recebe uma senha que pode ser vermelha, amarela, verde ou azul,
# conforme a gravidade do paciente. A senha de cor vermelha indica uma Emergência e, portanto,
# tem a maior prioridade de atendimento, pois há risco de morte imediato (ex. paciente com
# parada cardiorrespiratória, trauma de crânio, crise convulsiva, choque elétrico, derrame,
# hemorragia, etc.). A senha amarela indica Urgência e tem a segunda maior prioridade de
# atendimento (até meia hora no máximo). O paciente pode apresentar um quadro de dor intensa
# (de início imediato), luxação, sangramento, desmaios, etc. A senha de cor verde é para pacientes
# pouco urgentes, que podem esperar pelo atendimento ambulatorial, com prioridade sobre o
# não urgente, que podem aguardar por até 4 horas para serem atendidos (ex. pacientes acima
# de 60 anos, deficientes físicos, pacientes com vômito e diarreia). A senha azul é para pacientes
# não urgentes, que podem aguardar por até 6 horas para serem atendidos(ex., exames de rotina,
# acompanhamento de doenças crônicas, troca de receitas, etc.).

# A aplicação deverá manter duas filas em listas: uma para senhas de cores Vermelha e Amarela
# (Emergência e Urgência) e outra para os atendimentos ambulatoriais (ou seja, para senhas de
# cores verde e azul). O programa deverá apresentar para o usuário um menu com as opções a
# seguir e implementar cada opção:

# Menu de Opções:

# 1 – Inserir paciente na fila de Emergência e Urgência
# 2 – Inserir paciente na fila de Atendimento Ambulatorial (Pouco urgente e não urgente)
# 3 – Atender paciente com Emergência ou Urgência
# 4 – Atender paciente no Ambulatório
# 5 – Imprimir fila de Emergência e Urgência
# 6 – Imprimir fila de Atendimento Ambulatorial
# 7 – Sair da aplicação

# Para a opção 1 do Menu, considere que pacientes em Emergência serão os primeiros da fila e os
# pacientes em Urgência serão os últimos da fila, respeitando-se a ordem de chegada dos
# pacientes (por ex. “VE01, VE02, AM01, AM02, AM03, ...”). Para a opção 2 do Menu, considere
# que pacientes com pouca urgência serão os primeiros da fila, enquanto que os pacientes não
# urgentes serão os últimos da fila (por ex. “VER01, VER02, VER03, AZ01, AZ02, AZ03, ...”).
                                   
# Quando as opções 3 e 4 do Menu forem escolhidas (ou seja, quando o paciente for chamado
# para o atendimento), a senha chamada deverá ser removida da fila. As opções 5 e 6 do Menu
# devem apresentar todas as senhas armazenadas nas filas naquele momento.
# O programa somente deverá ser encerrado quando a opção 7 do Menu foi escolhida.


fila_emergencia_urgencia = []
fila_ambulatorial = []


def mostrar_menu():
    print("\n--- MENU DE OPÇÕES ---")
    print("1 – Inserir paciente na fila de Emergência e Urgência")
    print("2 – Inserir paciente na fila de Atendimento Ambulatorial")
    print("3 – Atender paciente com Emergência ou Urgência")
    print("4 – Atender paciente no Ambulatório")
    print("5 – Imprimir fila de Emergência e Urgência")
    print("6 – Imprimir fila de Atendimento Ambulatorial")
    print("7 – Sair da aplicação")
    return int(input("Escolha uma opção: "))

def inserir_emergencia_urgencia():
    cor = input("Digite a cor (Vermelha ou Amarela): ").strip().lower()
    if cor == "vermelha":
        fila_emergencia_urgencia.insert(0, f"VE{len(fila_emergencia_urgencia)+1}")
    elif cor == "amarela":
        fila_emergencia_urgencia.append(f"AM{len(fila_emergencia_urgencia)+1}")
    else:
        print("Cor inválida!")

def inserir_ambulatorial():
    cor = input("Digite a cor (Verde ou Azul): ").strip().lower()
    if cor == "verde":
        fila_ambulatorial.insert(0, f"VER{len(fila_ambulatorial)+1}")
    elif cor == "azul":
        fila_ambulatorial.append(f"AZ{len(fila_ambulatorial)+1}")
    else:
        print("Cor inválida!")

def atender_emergencia():
    if fila_emergencia_urgencia:
        print("Atendido:", fila_emergencia_urgencia.pop(0))
    else:
        print("Fila de emergência está vazia.")

def atender_ambulatorial():
    if fila_ambulatorial:
        print("Atendido:", fila_ambulatorial.pop(0))
    else:
        print("Fila ambulatorial está vazia.")

def imprimir_emergencia():
    print("Fila Emergência/Urgência:", fila_emergencia_urgencia)

def imprimir_ambulatorial():
    print("Fila Ambulatorial:", fila_ambulatorial)


def sistema_upa():
    while True:
        opcao = mostrar_menu()
        if opcao == 1:
            inserir_emergencia_urgencia()
        elif opcao == 2:
            inserir_ambulatorial()
        elif opcao == 3:
            atender_emergencia()
        elif opcao == 4:
            atender_ambulatorial()
        elif opcao == 5:
            imprimir_emergencia()
        elif opcao == 6:
            imprimir_ambulatorial()
        elif opcao == 7:
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")


sistema_upa()




