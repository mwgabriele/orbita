import controller

#def cadastrar_missao():
    # receber os dados do usuário
    #print("Cadastrar Missão Espacial")
    #nome_missao = input("Nome da missão: ")
    #veiculo_lancador = input("Veículo lançador: ")

    #controller.cadastrar_missao(nome_missao, veiculo_lancador)

def consultar_missao():
    print("\nConsultar Missão Espacial:")

    nome_missao = input("Nome da missão: ")

    nome_missao, veiculo_de_lancamento = controller.consultar_missao(nome_missao)

    print(f"Veículo de lançamento da missão {nome}: {veiculo}")