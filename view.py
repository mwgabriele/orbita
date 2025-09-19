import controller

def cadastrar_missao():
    # receber os dadods do usuario
    print("Cadastrar Missão Espacial")
    nome_missao = input("Nome: ")
    veiculo_lancador = input("Veiculo lancador: ")

    controller.cadastrar_missao(nome_missao, veiculo_lancador)

def consultar_missao():
    print("\nConsultar Missão Espacial:")

    nome = input("Nome da missão: ")

    nome_missao, veiculo_lancador = controller.consultar_missao(nome)

    print(f"Veículo: {veiculo}")