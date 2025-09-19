import sqlite3

class Missao:
    def __init__(self, nome_missao, veiculo_lancador):
        self.nome_missao = nome_missao
        self.veiculo_lancador = veiculo_lancador

####################################

def cadastrar_missao(missao:Missao):
    sql = '''
        INSERT INTO lancamentos_espaciais (nome_missao, veiculo_lancador)
        VALUES (?, ?);
    '''
    with sqlite3.connect("missoes.db") as conexao:
        conexao.execute(sql, (missao.nome_missao, missao.veiculo_lancador))

def consultar_missao(missao):
    sql = '''
    SELECT nome_missao, veiculo_lancador
    FROM lancamentos_espaciais
    WHERE nome_missao = ?;
    '''
    with sqlite3.connect("missoes.db") as conexao:
        cursor = conexao.execute(sql, (missao.nome_missao,))
        _, veiculo = cursor.fetchone()
        missao.nome_missao = nome
        missao.veiculo_veiculo = veiculo
        # agora começa a viagem de volta dos dados, ate a view/usuario

    # retornamos para a model os dados da consulta 
    return missao


with sqlite3.connect("missoes.db") as conexao:
    sql_create_table_lancamentos_espaciais = '''
    CREATE TABLE IF NOT EXISTS lancamentos_espaciais (
        id INTEGER PRIMARY KEY NOT NULL,
        nome_missao TEXT,
        veiculo_lancador TEXT
    );
    '''
    conexao.execute(sql_create_table_lancamentos_espaciais)