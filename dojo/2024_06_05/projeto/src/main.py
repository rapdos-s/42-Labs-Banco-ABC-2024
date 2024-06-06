import sqlite3
import random

projects = [
    {"name": "libft", "phase": 1},
    {"name": "get_next_line", "phase": 1},
    {"name": "ft_printf", "phase": 1},
    {"name": "Born2beroot", "phase": 1},
    {"name": "fdf", "phase": 1},
    {"name": "fractol", "phase": 1},
    {"name": "so_long", "phase": 1},
    {"name": "minitalk", "phase": 1},
    {"name": "pipex", "phase": 1},
    {"name": "push_swap", "phase": 2},
    {"name": "minishell", "phase": 2},
    {"name": "Philosophers", "phase": 2},
    {"name": "NetPractice", "phase": 2},
    {"name": "cub3d", "phase": 2},
    {"name": "mini_RT", "phase": 2},
    {"name": "CPP Module 00", "phase": 3},
    {"name": "CPP Module 01", "phase": 3},
    {"name": "CPP Module 02", "phase": 3},
    {"name": "CPP Module 03", "phase": 3},
    {"name": "CPP Module 04", "phase": 3},
    {"name": "CPP Module 05", "phase": 3},
    {"name": "CPP Module 06", "phase": 3},
    {"name": "CPP Module 07", "phase": 3},
    {"name": "CPP Module 08", "phase": 3},
    {"name": "CPP Module 09", "phase": 3},
    {"name": "Inception", "phase": 3},
    {"name": "webserv", "phase": 3},
    {"name": "ft_irc", "phase": 3},
    {"name": "ft_transcendence", "phase": 3},
]


def run_tests(tests, conn):
    for index, test in enumerate(tests):
        result = test["function"](conn)
        if result == test["expected_value"]:
            print(f"🟢 [Test {index} OK] {test['description']}")
        else:
            print(f"🔴 [Test {index} KO] {test['description']}")
            print(f"\tresult        : {result}")
            print(f"\texpected value: {test['expected_value']}")


def create_database():
    db_name = "/app/volumes/db_name"
    conn = sqlite3.connect(db_name)

    return conn


def create_tables(conn):
    cur = conn.cursor()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS cadets(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL,
        id_projects INTEGER NOT NULL,
        FOREIGN KEY (id_projects) REFERENCES projects(id)
        )"""
    )

    cur.execute(
        """CREATE TABLE IF NOT EXISTS projects(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phase INTEGER NOT NULL
        )"""
    )


def populate_cadets_table(conn):
    cur = conn.cursor()
    logins = [
        "dmoreira",
        "lumedeir",
        "adantas-",
        "carrodri",
        "csantos-",
        "csouza-f",
        "fnacarel",
        "kdaiane-",
        "lade-lim",
        "lamorim",
        "luizedua",
        "mamacedo",
        "namoreir",
        "pdavi-al",
        "r-leite",
        "rabustam",
        "rapdos-s",
        "rede-and",
        "telias-p",
        "vcedraz-",
    ]

    project_ids = [index for index, project in enumerate(projects)]
    for login in logins:
        project_id = random.choice(project_ids)
        cur.execute('INSERT INTO cadets (login, id_projects) VALUES (?, ?)', (login, project_id))


def populate_projects_table(conn):
    cur = conn.cursor()

    for project in projects:
        cur.execute('INSERT INTO projects (name, phase) VALUES (?, ?)', (project["name"], project["phase"]))


def get_table(conn):
    cur = conn.cursor()

    test = cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence'"
    )
    tables_tupla = cur.fetchall()
    tables_list = []

    for table in tables_tupla:
        tables_list.append(table[0])
    return tables_list


if __name__ == "__main__":
    testes = [
        {
            "function": get_table,
            "expected_value": ["foo", "bar"],
            "description": "This must be an error",
        },
        {
            "function": get_table,
            "expected_value": ["cadets", "projects"],
            "description": "Check database's tables created",
        },
    ]
    database_connection = create_database()

    create_tables(database_connection)

    run_tests(testes, database_connection)
    populate_cadets_table(database_connection)
    populate_projects_table(database_connection)
