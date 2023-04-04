#Programa para verificar se um ano é bissexto

year = int(input("Digite o ano que deseja saber se é bissexto: "))

restoDivisao = year % 4

restoDivisao100 = year % 100

if restoDivisao == 0 and restoDivisao100 != 0:
    print("Esse ano é bissexto!")
else:
    print("Esse ano não é bissexto!")