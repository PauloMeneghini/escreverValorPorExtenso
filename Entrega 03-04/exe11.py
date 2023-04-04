# Desenvolva um algoritmo e efetue a implementação em Python para ler
# dois valores (inicial e final) de um intervalo e indique os números que são
# divisíveis por 3.

valorInicial = int(input("Digite o primeiro valor inteiro: "))
valorFinal = int(input("Digite o segundo valor inteiro: "))

if valorInicial > valorFinal:
    valorInicial, valorFinal = valorFinal, valorInicial

for x in range(valorInicial, valorFinal+1):
    
    restoDivisao = x % 3

    if restoDivisao == 0:
        print("\nO número {} é divisivel por 3".format(x))
    else:
        print("\nO número {} não é divisivel por 3".format(x))