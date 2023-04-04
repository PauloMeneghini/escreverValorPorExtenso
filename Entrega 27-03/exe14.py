#Programa para veririficar se as datas estão corretas

dataInvalida = True

while dataInvalida == True:

    days = int(input("Digite o dias: "))
    month = int(input("Digite o mês: "))
    year = int(input("Digite o ano: "))

    if days > 31:
        print("O maximo de dias é 31!")
    else:
        if month == 2:
            if days > 28:
                print("Data invalida!")
            else:
                print("Data valida!")
                print("{}/{}/{}".format(days, month, year))
                dataInvalida = False

        if month == 4 or month == 6 or month == 0 or month == 11:
            if days > 30:
                print("Data invalida!")
            else:
                print("Data valida!") 
                print("{}/{}/{}".format(days, month, year))
                dataInvalida = False

        print("Data valida!") 
        print("{}/{}/{}".format(days, month, year))
        dataInvalida = False