import random

numeroComputador=random.randint(0,100)

print("JOGO: ADIVINHE O NÚMERO (0 a 100)")
print(numeroComputador)

numeroJogador=-1
contTentativas = 0

while  True:

    numeroJogador=int(input("DIGITE UM NÚMERO: "))

    if(numeroJogador > numeroComputador):

        print("\nO seu número é MAIOR que o do computador\n")

    if(numeroJogador < numeroComputador ):

        print("\nO seu número é MENOR que o do computador\n")

    if(numeroJogador==numeroComputador ):
        print("\nPARABÉNS, VOCÊ ACERTOU O NÚMERO")
        print("Numeros de tentativas: {}".format(contTentativas))
        break

    contTentativas += 1

    resposta = ""

    while resposta != "S":

        resposta = input("Deseja continuar jogando? (S - Sim | N - Não) ").upper()

        if resposta == "N":

            respostaNovoJogo = ""

            while respostaNovoJogo != "S":

                respostaNovoJogo = input("Deseja Iniciar um novo jogo? (S - Sim | N - Não) ").upper()

                if resposta == "N":
                    exit()
                
                if resposta != "S":
                    print("Digte S - Sim | N - Não")
        
        if resposta != "S":
            print("Digte S - Sim | N - Não")

    

