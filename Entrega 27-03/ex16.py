from num2words import num2words

numero = float(input('Digite um número: '))

num_ptbr = num2words(numero, lang='pt-br')
print(f'\nNúmero: {num_ptbr}\n')