import sqlite
import mensagens as msg

def main():
    NOVA_TAREFA = 1
    CONCLUIR_TAREFA = 2
    EXCLUIR_TAREFA = 3

    while True:
        msg.exibir_cabecalho()
        msg.exibir_tarefas()
        try:
            opcao = int(input("O que deseja fazer?\n 1 = Nova tarefa\n 2 = Concluir tarefa \n 3 = excluir tarefa"))
            if opcao == NOVA_TAREFA:
                msg.mostrar_opcao_nova_tarefa()
            elif opcao == CONCLUIR_TAREFA:
                msg.mostrar_concluir()
            elif opcao == EXCLUIR_TAREFA:
                msg.excluir_tarefa()
            else:
                print("Opção não reconhecida, por favor informe um número.")
        except ValueError as e:
            print("Opção não reconhecida, por favor informe um número.")
        except Exception:
            exit(0)

if __name__ == "__main__":
    sqlite.criar_table_todo()  # Adicione parênteses para chamar a função

    main()