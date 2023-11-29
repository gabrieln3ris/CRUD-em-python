import sqlite  # Certifique-se de que o módulo sqlite esteja disponível no seu ambiente

MENU_INICIAL = 99

def exibir_cabecalho():
    QTD_COLUNAS = 60
    print("-" * QTD_COLUNAS)
    print("{:^60}".format("TAREFAS"))
    print("-" * QTD_COLUNAS)
    print("{:^60}".format("tecle 99 volta para o menu inicial, [CTRL+C] sai"))
    print("-" * QTD_COLUNAS)

def exibir_tarefas():
    for tarefa in sqlite.get_tarefas():
        check = u'\u2713' if tarefa[2] == 1 else ""
        t = "- [{:>4}] {:<47} {:^3}".format(tarefa[0], tarefa[1], check)
        print(t)
    print("-" * 60)

def mostrar_opcao_nova_tarefa():
    texto_nova_tarefa = input("Descreva a tarefa: ")
    print("Adicionando tarefa -> " + str(texto_nova_tarefa))
    if texto_nova_tarefa != str(MENU_INICIAL):
        sqlite.add_tarefa(texto_nova_tarefa)

def mostrar_concluir():
    cd_tarefa = int(input("Qual tarefa deseja concluir? Digite o código => "))
    print("Concluindo tarefa -> " + str(cd_tarefa))
    if cd_tarefa != MENU_INICIAL:
        sqlite.concluir_tarefa(cd_tarefa)

def excluir_tarefa():
    cd_tarefa = int(input("qual tarefa vc deseja excluir da lista? Digite o Codigo =>"))
    print('excluindo tarefa -> ' + str(cd_tarefa))
    sqlite.remover_tarefa(cd_tarefa)