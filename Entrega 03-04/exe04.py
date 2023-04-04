# Desenvolva um algoritmo e efetue a implementação em Python para
# calcular a fatorial de um número n

def fatorial(valor):
    fatorial = 1
    for i in range(1, valor + 1):
        fatorial *= i
    return fatorial
    
number = int(input("Digite um número: "))

print(fatorial(number))