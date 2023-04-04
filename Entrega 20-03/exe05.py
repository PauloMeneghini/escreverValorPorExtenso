prova1 = float(input("\nDigite a nota da primeira prova: "))
peso1 = float(input("\nDigite o peso da primeira prova: "))
prova2 = float(input("\nDigite a nota da segunda prova: "))
peso2 = float(input("\nDigite o peso da segunda prova: "))

media = ((prova1 * peso1) + (prova2 * peso2)) / (peso1 / peso2)

if media < 5:
    print("\nReprovado\n")
elif media >= 5:
    print("\nAprovado\n")
    if media >= 8 and media < 9:
        print("PARABÉNS O DESEMPENHO FOI MUITO BOM\n")
    elif media >= 9:
        print("PARABÉNS, VOCÊ FOI APROVADO COM LOUVOR\n")