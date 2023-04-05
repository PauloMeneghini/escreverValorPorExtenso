#from num2words import num2words

valorDigitado = input("Digite um valor (Separando por ',' a casa dos centavos): ")

print(valorDigitado)
print(type(valorDigitado))

valor = valorDigitado.split(",")
valorReal = int(valor[0])
valorCentavo = int(valor[1])

unidadeCentavo=int(valorCentavo%10)
dezenaCentavo=int((valorCentavo-unidadeCentavo)/10)%10

print(dezenaCentavo)
print(unidadeCentavo)


# ESCREVE EXTENSO REAL 

if valorReal == 1:
    auxiliarReal = "um"
elif valorReal == 2:
    auxiliarReal = "dois"
elif valorReal == 3:
    auxiliarReal = "três"
elif valorReal == 4:
    auxiliarReal = "quatro"
elif valorReal == 5:
    auxiliarReal = "cinco"
elif valorReal == 6:
    auxiliarReal = "seis"
elif valorReal == 7:
    auxiliarReal = "sete"
elif valorReal == 8:
    auxiliarReal = "oito"
elif valorReal == 9:
    auxiliarReal = "nove"

if valorReal == 1:
    textoReal = " real"
else:
    textoReal = " reais"

# ESCREVE EXTENSO CENTAVOS 

if dezenaCentavo == 1:
    if unidadeCentavo == 0:
        auxDezenaCentavo = "dez"
    if unidadeCentavo == 1:
        auxDezenaCentavo = "onze"
    if unidadeCentavo == 2:
        auxDezenaCentavo = "doze"
    if unidadeCentavo == 3:
        auxDezenaCentavo = "treze"
    if unidadeCentavo == 4:
        auxDezenaCentavo = "quatorze"
    if unidadeCentavo == 5:
        auxDezenaCentavo = "quinze"
    if unidadeCentavo == 6:
        auxDezenaCentavo = "dezesseis"
    if unidadeCentavo == 7:
        auxDezenaCentavo = "dezessete"
    if unidadeCentavo == 8:
        auxDezenaCentavo = "dezoito"
    if unidadeCentavo == 9:
        auxDezenaCentavo = "dezenove"    
else:     
    if dezenaCentavo == 2:
        auxDezenaCentavo = "vinte"
    if dezenaCentavo == 3:
        auxDezenaCentavo = "trinta"
    if dezenaCentavo == 4:
        auxDezenaCentavo = "quarenta"
    if dezenaCentavo == 5:
        auxDezenaCentavo = "cinquenta"
    if dezenaCentavo == 6:
        auxDezenaCentavo = "sessenta"
    if dezenaCentavo == 7:
        auxDezenaCentavo = "setenta"
    if dezenaCentavo == 8:
        auxDezenaCentavo = "oitenta"
    if dezenaCentavo == 9:
        auxDezenaCentavo = "noventa"
    
    
    # if unidadeCentavo==0:
    #     auxunidadeCentavo="zero"
    if unidadeCentavo == 1:
        auxUnidadeCentavo = "um"
    if unidadeCentavo == 2:
        auxUnidadeCentavo = "dois"
    if unidadeCentavo == 3:
        auxUnidadeCentavo = "três"
    if unidadeCentavo == 4:
        auxUnidadeCentavo = "quatro"
    if unidadeCentavo == 5:
        auxUnidadeCentavo = "cinco"
    if unidadeCentavo == 6:
        auxUnidadeCentavo = "seis"
    if unidadeCentavo == 7:
        auxUnidadeCentavo = "sete"
    if unidadeCentavo == 8:
        auxUnidadeCentavo = "oito"
    if unidadeCentavo == 9:
        auxUnidadeCentavo = "nove"

valorCentavoExtenso = "{} e {}".format(auxDezenaCentavo, auxUnidadeCentavo)


if valorCentavo == 1:
    textoCentavos = " centavo"
else:
    textoCentavos = " centavos"

if valorReal > 0:
    textoValorReal = auxiliarReal + textoReal
else:
    textoReal = ""

if valorCentavo > 0:
    textoValorCentavo = valorCentavoExtenso + textoCentavos
else:
    textoValorCentavo = ""

if valorReal > 0 and valorCentavo > 0:
    resultado = textoValorReal + " e " + textoValorCentavo
else:
    resultado = textoValorReal + textoValorCentavo

print("\n")
print(resultado)
print("\n")