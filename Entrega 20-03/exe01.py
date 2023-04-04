# Desenvolver um algoritmo e implementar em Python, para efetuar a leitura
# de uma senha numérica, efetuar a sua validação (senha pré-cadastrada)

password = int(input("\nDigite a senha do sistema: "))

if password == 1234:
    print("\nACESSO PERMITIDO\n")
else:
    print("\nACESSO NEGADO\n")