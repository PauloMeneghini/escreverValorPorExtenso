#Programa para calcular salario liquido descontando IR

salario = float(input("\nDigite seu salário bruto: "))

ir = 0

if salario > 1903.99:
    ir = salario * 0.075
elif salario > 2826.66: 
    ir = salario * 0.15
elif salario > 3751.06:
    ir = salario * 0.225
elif salario > 4664.68:
    ir = salario * 0.275
else:
    print("\nNão à IR sobre seu salário\n")
    exit()

salarioLiquido = salario - ir

print(salarioLiquido)