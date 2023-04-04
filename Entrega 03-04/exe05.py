# Desenvolva um algoritmo e efetue a implementação em Python para
# imprimir a tabuada de um número n:

numero = int(input("Digite o valor que deseja saber a tabuada: "))

for i in range(10):
    mult = numero * (i + 1)
    print("{} x {} = {}".format(numero, (i + 1), mult))