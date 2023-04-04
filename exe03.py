# Valor do bem a ser segurado ( VSB ) 
# Número de usuário ( USER )
# Taxa de seguro ( TS )
# Taxa de desconto ( DS )
# Número de parcelas ( NP )

VSB = float(input("Digite o valor do bem a ser segurado: "))
user = int(input("Digite a quantidade de usuários que utilizam o bem: "))
TS = float(input("Digite a taxa do seguro: "))
DS = float(input("Digite a quantidade de desconto: "))
NP = int(input("Digite a quantidade de parcelas: "))

VSEG = VSB * TS/100

VUSER = VSEG * user/100

DS = (VSEG + VUSER) * DS/100

SEG = VSEG + VUSER - DS

VPARCELA = SEG / NP

print("O valor do seguro é: {}".format(VSEG))
print("O valor do usuário é: ".format(VUSER))
print("O desconto é: {}".format(DS))
print("O valor do seguro liquido é: {}".format(SEG))
print("O valor da parcela é: {}".format(VPARCELA))