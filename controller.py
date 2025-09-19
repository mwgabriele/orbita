import model

def cadastrar_missao(nome_missao, veiculo_lancador):
    nova_missao = model.Missao(nome_missao, veiculo_lancador)

    model.cadastrar_missao(nova_missao)

def consultar_missao(nome_missao):
    missao = model.Missao(nome_missao, None)
    resposta = model.consultar_missao(missao)

     # retornando dados para a view  na forma de objetor (Produto)
    return (resposta.nome, resposta.veiculo) # retornandop dados desestruturados para a view