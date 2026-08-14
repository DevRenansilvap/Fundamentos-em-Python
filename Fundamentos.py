#Fundamentos em Python 

# Modulo : Variaveis , tipos de Dados e strings

nome = "Renan"
idade = 23
altura = 1.80

print(f"Meu nome é {nome} eu tenho {idade} e tenho {altura} de altura")

# Peça ao usuário para digitar dois números (use input()).
# Converta ambos para int e imprima a soma, subtração, multiplicação e divisão.

num1 = input("Digite o Primeiro numero:")
num2 = input("Digite o Segundo numero:")

soma = int(num1)+int(num2)
subtracao = int(num1)-int(num2)
multiplicacao = int(num1)*int(num2)
divisao = int(num1)/int(num2)

print(f"A soma é:{soma} a subtração é:{subtracao} a multiplicacao é:{multiplicacao} a divisao é:{divisao}")

