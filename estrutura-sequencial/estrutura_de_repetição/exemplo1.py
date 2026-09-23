# # num = int(input("Digite um numero positivo:"))

# # while num <= 0:
# #     print("Numero ibnvalido Tente nvamente")
# #     num =int(input("Digite um numero positivo novamente"))
# # print(f"o numero digitado é:{num}")

# # cont = 0
# # while cont < 10:
# #     cont = cont + 1
# #     print(f"Contador: {cont}")
# #     if (cont == 5):
# #         break
# # print("Fim!")

# while True:
#     idade = int(input("Qual a sua idade:"))
#     if (idade > 0 ):
#         print(f"Sua idade é{idade}")
#         break
# print   ' '

# num = 5
# num2 = 4
# while True:
#     print(num * num2)
#     num2 = num2 + 1
#     if (num2 >=  7):
#         break
# valor_tabuada = int(input("Montar tabuada de:"))
# comeco = int(input("começar por:"))
# termino = int(input("Termina em:"))

# while True:
#     print(f"Valor Tabuada: {valor_tabuada} * {comeco} = {comeco * valor_tabuada}")
#     comeco = comeco + 1
#     if (comeco > termino):
#         break
# print("Fim!")

cand_1 = 0
cand_2 = 0
cand_3 = 0
cand_4 = 0
nulo = 0
branco = 0


while True:
    voto = int(input("Digite o seu voto:"))
    if voto > 7 or voto < 0:
           print("Numero Invalido, Digite um Numero Válido")
    else: 
        if voto == 1:
            cand_1 = cand_1 +1
            print ("Voto confirmado!")
        elif voto == 2:
            cand_2 = cand_2 +1
            print ("Voto confirmado!")
        elif voto == 3:
            cand_3 = cand_3 +1
            print ("Voto confirmado!")
        elif voto == 4:
            cand_4 = cand_4 +1
            print ("Voto confirmado!")
        elif voto == 5:
            nulo = nulo +1
            print ("Voto confirmado!")
        elif voto == 6:
            branco = branco +1
            print ("Voto confirmado!")
        if voto == 0:
            break
total_votos = (cand_1 + cand_2 + cand_3 + cand_4 +nulo + branco)
if total_votos ==0:
    total_votos= 1
print (f"""
    candidato 1:{(cand_1 / total_votos)*100:.2f}%
    candidato 2:{(cand_2 / total_votos)*100:.2f}%
    candidato 3:{(cand_3 / total_votos)*100:.2f}%
    candidato 4:{(cand_4 / total_votos)*100:.2f}%
    nulo:{(nulo / total_votos)*100:.2f}%
    branco:{(branco / total_votos)*100:.2f}%
""")