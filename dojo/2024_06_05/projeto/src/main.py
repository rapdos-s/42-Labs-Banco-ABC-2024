import sqlite3

# def database():
#     print("Criando banco de dados...")
#     db_name = "/app/volumes/db_name"

#     print("Abrindo banco de dados...")
#     conn = sqlite3.connect(db_name)

#     cur = conn.cursor()

#     cur.execute('''CREATE TABLE IF NOT EXISTS cadetes(
#         name TEXT NOT NULL)''')
#     nome = "qualquer"
#     cur.execute(f'''INSERT INTO cadetes(name) VALUES('{nome}')''')
#     cur.execute('''INSERT INTO cadetes(name) VALUES('Bianca')''')
#     cur.execute('''INSERT INTO cadetes(name) VALUES('Carlos')''')
#     cur.execute('''SELECT * FROM cadetes''')

#     toprint = cur.fetchall()

#     print(toprint)

def cria_banco():
    db_name = "/app/volumes/db_name"
    conn = sqlite3.connect(db_name)

    return conn

def cria_tabelas(conn):
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS cadetes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS projetos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
        )''')
def popula_tabela_cadetes(conn, login):
    cur = conn.cursor()
    logins = ["rapdos-s", "dmoreira", "lumedeir", "luizedua"]
    for login in logins:
        cur.execute(f'''INSERT INTO cadetes(login) VALUES('{login}')''')


def popula_tabela_projetos(conn, name):
    cur = conn.cursor()
    projetos = ["ft_irc", "minishell", "ft_transcendence", "libasm"]
    for projeto in projetos:
        cur.execute(f'''INSERT INTO projetos(name) VALUES('{projeto}')''')

def pega_tabelas(conn):
    cur = conn.cursor()

    test = cur.execute("SELECT name FROM sqlite_master")
    tables_tupla = cur.fetchall()
    tables_list = []

    for table in tables_tupla:
        tables_list.append(table[0])
    return tables_list

if __name__ == "__main__":
    conexao_banco = cria_banco()
    cria_tabelas(conexao_banco)
    print(pega_tabelas(conexao_banco))
