# Desenvolva um algoritmo e efetue a implementação em Python para ler n
# valores e imprimir o valor médio.

qtdNumeros = int(input("Quantos números quer digitar? "))

somaValores = 0

for x in range(qtdNumeros):
    valor = float(input("Digite o {}º valor: ".format((x + 1))))
    somaValores += valor

media = somaValores / qtdNumeros

print("A média dos valores são: {}".format(media))