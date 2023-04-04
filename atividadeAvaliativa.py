#from num2words import num2words

def escreveExtenso(valor):

    auxiliar = ""

    if valor == 1:
        auxiliar = "um"
    elif valor == 2:
        auxiliar = "dois"
    elif valor == 3:
        auxiliar = "três"
    elif valor == 4:
        auxiliar = "quatro"
    elif valor == 5:
        auxiliar = "cinco"
    elif valor == 6:
        auxiliar = "seis"
    elif valor == 7:
        auxiliar = "sete"
    elif valor == 8:
        auxiliar = "oito"
    elif valor == 9:
        auxiliar = "nove"

    return auxiliar

def converteValor(valor):
        
    valor = valor.split(",")
    valorReal = int(valor[0])
    valorCentavo = int(valor[1])

    resultadoReal = escreveExtenso(valorReal)

    if valorReal == 1:
        textoReal = " real"
    else:
        textoReal = " reais"

    # if valorCentavo == 1:
    #     textoCentavos = " centavo"
    # else:
    #     textoCentavos = " centavos"

    if valorReal > 0:
        textoValorReal = resultadoReal + textoReal
    else:
        textoReal = ""

    # if valorCentavo > 0:
    #     textoValorCentavo = num2words(valorCentavo, lang='pt_BR') + textoCentavos
    # else:
    #     textoValorCentavo = ""

    if valorReal > 0 and valorCentavo > 0:
        resultado = textoValorReal #+ " e " + textoValorCentavo
    else:
        resultado = textoValorReal #+ textoValorCentavo

    return resultado
    

valorDigitado = input("Digite um valor (Separando por ',' a casa dos centavos): ")

print("\n")
print(converteValor(valorDigitado))
print("\n")