nota1 = float(input("Digite a Nota 1: "))
nota2 = float(input("Digite a Nota 2: "))
peso1 = float(input("Digite a Peso 1: "))
peso2 = float(input("Digite a Peso 2: "))

MedP = ((nota1 * peso1 + nota2 * peso2)/ (peso1 + peso2) )
print(f'A media Ponderada é igual a :{MedP:.2f}')