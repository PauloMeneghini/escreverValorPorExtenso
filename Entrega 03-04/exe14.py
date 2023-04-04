import random

while True:
    computador = int(random.randint(0,301)/100)

    jogador = None

    while jogador not in [0, 1, 2]:

        jogador = int(input("\nEscolha uma das três opções (0 - Pedra | 1 - Papel | 2 - Tesoura): "))

        if jogador not in [0, 1, 2]:
            print("\nEscolha uma opção valida")

    print(computador)
    print(jogador)

    qtdPontosComputador = 0
    qtdPontosJogador = 0

    if jogador == computador:
        print("Empatou!")
    elif jogador == 0 and computador == 1:
        print("Você perdeu!")
        qtdPontosComputador += 1
    elif jogador == 1 and computador == 2:
        print("Você perdeu!")
        qtdPontosComputador += 1
    elif jogador == 2 and computador == 0:
        print("Você perdeu!")
        qtdPontosComputador += 1
    elif jogador == 1 and computador == 0:
        print("Você ganhou!")
        qtdPontosJogador += 1
    elif jogador == 2 and computador == 1:
        print("Você ganhou!")
        qtdPontosJogador += 1
    elif jogador == 0 and computador == 2:
        print("Você ganhou!")
        qtdPontosJogador += 1
    

    resposta = ""

    while resposta != "S":

        resposta = input("Deseja continuar jogando? (S - Sim | N - Não) ").upper()

        if resposta == "N":
            print("Pontos jogador: {} \nPontos computador: {}".format(qtdPontosJogador, qtdPontosComputador))
            break
        
        if resposta != "S":
            print("Digte S - Sim | N - Não")