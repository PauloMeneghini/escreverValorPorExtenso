from num2words import num2words

def number_to_long_number(number_p):

    number_p = number_p.split(',')
    number_p1 = int(number_p[0].replace('.',''))
    number_p2 = int(number_p[1])
    print("A: {}".format(number_p1))
    print("B: {}".format(number_p2))

        
    if number_p1 == 1:
        aux1 = ' real'
    else:
        aux1 = ' reais'
        
    if number_p2 == 1:
        aux2 = ' centavo'
    else:
        aux2 = ' centavos'
        
    text1 = ''
    if number_p1 > 0:
        text1 = num2words(number_p1,lang='pt_BR') + str(aux1)
    else:
        text1 = ''
    
    if number_p2 > 0:
        text2 = num2words(number_p2,lang='pt_BR') + str(aux2) 
    else: 
        text2 = ''
    
    if (number_p1 > 0 and number_p2 > 0):
        result = text1 + ' e ' + text2
    else:
        result = text1 + text2

    return result

valorDigitado = input("Digite um valor: ")

print(number_to_long_number(valorDigitado))