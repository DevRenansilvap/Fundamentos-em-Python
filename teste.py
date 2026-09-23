qtd_hamburguer = int(input("Digite a quantidade de hamburguer:"))
qtd_refrigerantes = int(input("Digite a quantidade de refrigerantes:"))
qtd_batatas = int(input("Digite a quantidade de batatas:"))

valor_unitario_hamburguer = 18
valor_unitario_refri = 6
valor_unitario_batata = 9

# Processamento
preco_total = ((qtd_batatas*valor_unitario_batata) + (qtd_hamburguer * valor_unitario_hamburguer) + (qtd_refrigerantes* valor_unitario_refri) )


# Resultado
print (f"Total a ser pago é :{preco_total}")