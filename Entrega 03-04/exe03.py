# Utilizando o código do exercício anterior, desenvolva um algoritmo e
# efetue a implementação em Python para ler n valores e imprimir o valor
# médio, o maior e o menor valor.

qtdNumeros = int(input("Quantos números quer digitar? "))

somaValores = 0
maior = 0
menor = 9999999999

for x in range(qtdNumeros):
    valor = float(input("Digite o {}º valor: ".format((x + 1))))
    somaValores += valor

    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor

media = somaValores / qtdNumeros

print("A média dos valores são: {}".format(media))
print("O maior valor digitado foi: {}".format(maior))
print("O menor valor digitado foi: {}".format(menor))