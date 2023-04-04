# Desenvolver um algoritmo e efetuar a
# implementação em Python, para ler o
# comprimento dos 3 lados de um triângulo e
# indicar a sua classificar

lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if lado1 == lado2 and lado2 == lado3 and lado3 == lado1:
    print("\nEsse é um triângulo equilátero!\n")
elif lado1 == lado2 and lado2 == lado3 or lado3 == lado1 and lado1 == lado2:
    print("\nEsse é um triângulo isóscele!\n")
else:
    print("\nEsse é um triângulo escaleno!\n")