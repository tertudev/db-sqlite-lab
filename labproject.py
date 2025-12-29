import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(str(ROOT_PATH / 'my_bank.db'))
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()

def criar_tabela(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT
        )
    """)
    conexao.commit()

def inserir_registro(cursor, nome, email):
    data = (nome, email)
    cursor.execute("""
        INSERT INTO clientes (nome, email)
        VALUES (?, ?)
    """, data)
    conexao.commit()

def atualizar_registro(cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("""
        UPDATE clientes
        SET nome = ?, email = ?
        WHERE id = ?
    """, data)
    conexao.commit()

def excluir_registro(cursor, id):
    cursor.execute("""
        DELETE FROM clientes
        WHERE id = ?
    """, (id,))
    conexao.commit()
    renumerar_ids(conexao, cursor)  # Renumera IDs após exclusão

def inserir_varios_registros(cursor, dados):
    cursor.executemany("""
        INSERT INTO clientes (nome, email)
        VALUES (?, ?)
    """, dados)
    conexao.commit()

def recuperar_dados(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    cursor.execute("SELECT * FROM clientes ORDER BY nome")
    return cursor.fetchall()

def renumerar_ids(conexao, cursor):
    cursor.execute("""
        CREATE TABLE clientes_temp (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT
        )
    """)
    cursor.execute("""
        INSERT INTO clientes_temp (nome, email)
        SELECT nome, email
        FROM clientes
        ORDER BY id
    """)
    cursor.execute("DROP TABLE clientes")
    cursor.execute("ALTER TABLE clientes_temp RENAME TO clientes")
    conexao.commit()

criar_tabela(cursor)

dados = [
    ('Daniela Torrez', 'daniela@gmail.com'),
    ('Carolina Ribeiro', 'carolina@gmail.com'),
    ('Lucas Silva', 'lucas@gmail.com'),
    ('Mariana Costa', 'mariana@gmail.com'),
    ('Pedro Santos', 'pedro@gmail.com'),
    ('Fernanda Oliveira', 'fernanda@gmail.com'),
    ('Gustavo Lima', 'gustavo@gmail.com'),
    ('Carla Pereira', 'carla@gmail.com'),
    ('Rafael Almeida', 'rafael@gmail.com'),
    ('Juliana Martins', 'juliana@gmail.com'),
    ('Thiago Rocha', 'thiago@gmail.com'),
    ('Patrícia Fernandes', 'patricia@gmail.com'),
    ('Bruno Carvalho', 'bruno@gmail.com'),
    ('Aline Souza', 'aline@gmail.com'),
    ('Marcelo Nunes', 'marcelo@gmail.com')
]
inserir_varios_registros(cursor, dados)

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))

cliente = recuperar_dados(cursor, 2)
if cliente:
    print(dict(cliente))
else:
    print("Cliente não encontrado")

conexao.close()
