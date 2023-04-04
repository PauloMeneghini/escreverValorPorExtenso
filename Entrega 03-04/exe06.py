menorTemp = 9999999
diaMenorTemp = 0

for dia in range (31):
    temp = (0.011 * dia ** 3) - (0.3 * dia ** 2) + (0.04 * dia)
    if temp < menorTemp:
        menorTemp = temp
        diaMenorTemp = dia

print(menorTemp)
print(diaMenorTemp)
