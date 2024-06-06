import sqlite3
import random

def executa_teste(testes, conn):
    for index, teste in enumerate(testes):
        retorno = teste["funcao"](conn)
        if retorno == teste["valor_esperado"]:
            print(f"🟢 [Teste {index} OK] {teste["enunciado"]}")
        else:
            print(f"🔴 [Teste {index} KO] {teste["enunciado"]}")


def cria_banco():
    db_name = "/app/volumes/db_name"
    conn = sqlite3.connect(db_name)

    return conn


def cria_tabela_cadetes(conn):
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS cadetes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL,
        id_projeto INTEGER NOT NULL,
        FOREIGN KEY (id_projeto) REFERENCES projetos(id)
        )''')

    #teste = cur.execute("SELECT * FROM cadetes")
    #print(f">>>>>>>>>{teste.description}")
    # tabela_cadetes_tupla.fetchall()
    # tabela_cadetes_list = []

    # for table in tabela_cadetes_tupla:
    #     tabela_cadetes_list.append(table[0])
    # return tabela_cadetes_list


def cria_tabelas(conn):
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS projetos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        fase INTEGER NOT NULL
        )''')
    teste = cur.execute("SELECT * FROM projetos")
    print(f">>>>>>>>>{teste.description}")
    
    print(f"🤖: {cria_tabela_cadetes(conn)}")


def popula_tabela_cadetes(conn):
    cur = conn.cursor()
    logins = ["dmoreira", "lumedeir", "adantas-", "carrodri", "csantos-", "csouza-f", "fnacarel", "kdaiane-", "lade-lim", "lamorim", "luizedua", "mamacedo", "namoreir", "pdavi-al", "r-leite", "rabustam", "rapdos-s", "rede-and", "telias-p", "vcedraz-"]

    lista_indices = [ index for index, projeto in enumerate(projetos)]
    print(lista_indices)
    for login in logins:
        id_projeto = random.choice(lista_indices)
        cur.execute('INSERT INTO cadetes (login, id_projeto) VALUES (?, ?)', (login, id_projeto))
    print(f"PEGASUS: {cur.execute(f'''SELECT * FROM cadetes''').fetchall()}")



    # cur.execute(f'''INSERT INTO cadetes(login, id_projeto) VALUES('joao', '42')''')
      # cur.execute(f'''INSERT INTO projetos(name, fase) VALUES('{projeto["nome"], projeto["fase"]}')''')



projetos = [
    {"nome": "libft", "fase": 1},
    {"nome": "get_next_line", "fase": 1},
    {"nome": "ft_printf", "fase": 1},
    {"nome": "Born2beroot", "fase": 1},
    {"nome": "fdf", "fase": 1},
    {"nome": "fractol", "fase": 1},
    {"nome": "so_long", "fase": 1},
    {"nome": "minitalk", "fase": 1},
    {"nome": "pipex", "fase": 1},
    {"nome": "push_swap", "fase": 2},
    {"nome": "minishell", "fase": 2},
    {"nome": "Philosophers", "fase": 2},
    {"nome": "NetPractice", "fase": 2},
    {"nome": "cub3d", "fase": 2},
    {"nome": "mini_RT", "fase": 2},
    {"nome": "CPP Module 00", "fase": 3},
    {"nome": "CPP Module 01", "fase": 3},
    {"nome": "CPP Module 02", "fase": 3},
    {"nome": "CPP Module 03", "fase": 3},
    {"nome": "CPP Module 04", "fase": 3},
    {"nome": "CPP Module 05", "fase": 3},
    {"nome": "CPP Module 06", "fase": 3},
    {"nome": "CPP Module 07", "fase": 3},
    {"nome": "CPP Module 08", "fase": 3},
    {"nome": "CPP Module 09", "fase": 3},
    {"nome": "Inception", "fase": 3},
    {"nome": "webserv", "fase": 3},
    {"nome": "ft_irc", "fase": 3},
    {"nome": "ft_transcendence", "fase": 3}
    ]

def popula_tabela_projetos(conn, name):
    cur = conn.cursor()

    

    for projeto in projetos:
        cur.execute(f'''INSERT INTO projetos(name, fase) VALUES('{projeto["nome"], projeto["fase"]}')''')


def pega_tabelas(conn):
    cur = conn.cursor()

    test = cur.execute("SELECT name FROM sqlite_master")
    tables_tupla = cur.fetchall()
    tables_list = []

    for table in tables_tupla:
        tables_list.append(table[0])
    return tables_list


if __name__ == "__main__":
    testes = [
    {
        "funcao": pega_tabelas,
        "valor_esperado": ['cadetes', 'projetos'],
        "enunciado": "Verifica o nome das tabelas"
    },
    {
        "funcao": pega_tabelas,
        "valor_esperado": ['foo', 'bar'],
        "enunciado": "Isso aqui vai dar erro"
    }
    ]
    conexao_banco = cria_banco()

    cria_tabelas(conexao_banco)
    # print(pega_tabelas(conexao_banco))

    executa_teste(testes, conexao_banco)
    popula_tabela_cadetes(conexao_banco)
