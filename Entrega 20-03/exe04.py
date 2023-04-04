# Desenvolver um algoritmo e efetuar a implementação
# em Python, para ler dois números e informar se o
# primeiro é divisível pelo segundo.
# (NESTE CASO O RESTO DA DIVISÃO DEVE SER ZERO)

number1 = float(input("Digite o primeiro número: "))
number2 = float(input("Digite o segundo número: "))

if number1 % number2 == 0:
    print("O primeiro número é divisivel pelo segundo")
else:
    print("O primeiro número não é divisivel pelo segundo")