valorInicial = int(input("Digite o primeiro valor inteiro: "))
valorFinal = int(input("Digite o segundo valor inteiro: "))

valorDivisao = int(input("Digite o valor que deseja ser o divisivel: "))

if valorInicial > valorFinal:
    valorInicial, valorFinal = valorFinal, valorInicial

for x in range(valorInicial, valorFinal+1):
    
    restoDivisao = x % valorDivisao

    if restoDivisao == 0:
        print("\nO número {} é divisivel por {}".format(x, valorDivisao))
    else:
        print("\nO número {} não é divisivel por {}".format(x, valorDivisao))