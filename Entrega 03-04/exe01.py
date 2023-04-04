# Desenvolva um algoritmo e efetue a implementação em Python para ler
# dois valores e imprimir os valores inteiros no intervalo.

valorInicial = int(input("Digite o primeiro valor inteiro: "))
valorFinal = int(input("Digite o segundo valor inteiro: "))

if valorInicial > valorFinal:
    valorInicial, valorFinal = valorFinal, valorInicial

for x in range(valorInicial, valorFinal+1):
    print(x)
