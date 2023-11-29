import sqlite3

con = sqlite3.connect("todo-app.db")

def criar_table_todo():
    cursor = con.cursor()
    con.execute("""CREATE TABLE IF NOT EXISTS tarefa (
                    cd_tarefa INTEGER PRIMARY KEY AUTOINCREMENT,
                    tarefa TEXT,
                    concluido INTEGER
                )"""
               )    

def add_tarefa(tarefa):
    con.execute("INSERT INTO tarefa(tarefa, concluido) VALUES (?, 0)", (tarefa,))
    con.commit()

def remover_tarefa(cd_tarefa):
    con.execute("DELETE FROM tarefa WHERE cd_tarefa = ?", (cd_tarefa,))
    con.commit()

def concluir_tarefa(cd_tarefa):
    con.execute("UPDATE tarefa SET concluido = 1 WHERE cd_tarefa = ?", (cd_tarefa, ))
    con.commit()

def get_tarefas():
    return con.execute("SELECT cd_tarefa, tarefa, concluido FROM tarefa")