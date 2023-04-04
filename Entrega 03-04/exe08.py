import random

numeroComputador=random.randint(0,100)

print("JOGO: ADIVINHE O NÚMERO (0 a 100)")
print(numeroComputador)

numeroJogador=-1
contTentativas = 0

while  numeroJogador!=numeroComputador:

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
