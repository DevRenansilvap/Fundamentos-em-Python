#Fundamentos em Python 

# Modulo : Variaveis , tipos de Dados e strings

nome = "Renan"
idade = 23
altura = 1.80

print(f"Meu nome é {nome} eu tenho {idade} e tenho {altura} de altura")

# # Peça ao usuário para digitar dois números (use input()).
# # Converta ambos para int e imprima a soma, subtração, multiplicação e divisão.

num1 = input("Digite o Primeiro numero:")
num2 = input("Digite o Segundo numero:")

soma = int(num1)+int(num2)
subtracao = int(num1)-int(num2)
multiplicacao = int(num1)*int(num2)
divisao = int(num1)/int(num2)

print(f"A soma é:{soma} a subtração é:{subtracao} a multiplicacao é:{multiplicacao} a divisao é:{divisao}")

# # Usando a função type() para descobrir o tipo de variavel

a = 10
b = 3.14
c = "Python"
d = True
e = None

print(f"O tipo da variável a é: {type(a)}")
print(f"O tipo da variável b é: {type(b)}")
print(f"O tipo da variável c é: {type(c)}")
print(f"O tipo da variável d é: {type(d)}")
print(f"O tipo da variável e é: {type(e)}")

# # Usando slicing
nome = "Renan da Silva"
print(f"As três primeiras letras são:{nome[:3]}")
print(f"As três primeiras letras são:{nome[11:14]}")
print(f"As três primeiras letras são:{nome[::-1]}")

# # Metodos de Manipulação de Strings
nome = ' Renan da Silva '
print(nome.strip()) # Remove espaços em branco no início e no final da string
print(nome.upper()) # Converte a string para maiúsculas
print(nome.lower()) # Converte a string para minúsculas
print(nome.count("e")) # Conta quantas vezes a letra "e" aparece na string


#concatenação e interpolação de strings
nome = "Renan"
idade = 23
print("meu nome é " + nome + "eu tenho " + str(idade) + " anos")
print(f"meu nome é {nome} eu tenho {idade} anos")

frase = input("Digite uma frase:")
print(len(frase))
print('Tem Python' if "Python" in frase else 'Não tem Python')
print(frase.replace('renanzinho ', 'Renan da Silva',))

email = "renansilva@email.com"
position = email.find("@")
print(email[0:position]) # Retorna a parte do email antes do @
print(email[position+1:]) # Retorna a parte do email depois do @

# Exercício 9 (desafio)
# Escreva um pequeno programa que receba o nome de uma pessoa (input())
# e imprima o nome formatado assim: primeira letra maiúscula, resto minúsculo,
# mesmo que o usuário digite tudo em maiúsculas ou minúsculas.

nome = input("Digite seu nome: ").lower()  # Converte o nome para minúsculas
print(nome.capitalize())