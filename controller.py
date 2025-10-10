import model

def cadastrar_missao(nome_missao, veiculo_lancador):
    nova_missao = model.Missao(nome_missao, veiculo_lancador)

    model.cadastrar_missao(nova_missao)

def consultar_missao(nome_missao):
    missao = model.Missao(veiculo_lancamento, None)
    resposta = model.consult_missao(missao)

     # retornando dados para a view  na forma de objeto
    return (resposta.nome_missao, resposta.veiculo_lancamento) # retornando dados desestruturados para a view