#Uma string é um tipo de dados usado para armazenar informações de texto.
#São considerados tipos simples pois seus valores são compostos por uma sequência de caracteres, podendo conter números, letras e pontuações.

texto1= "olá mundo"
texto2= "olá mundo"

print(texto1)
print(type(texto2))

multilinha_simples= '''Olá esse aqui é o funcionamento de uma multilinha
simples'''

nome= "Daniel"

print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4])
print(nome[5])

print("---------------------------")

print(nome[-0])
print(nome[-1])
print(nome[-2])
print(nome[-3])
print(nome[-4])
print(nome[-5])

print("---------------------------")

print(nome[2:])
print(nome[-2:])

print("---------------------------")

texto = "Python é uma linguagem de programação de alto nível"

print(texto[13:29])


print("---------------------------")

linha= "-"

print (linha*28)

print(nome)

print (linha*28)

#Fstrings

print(f'O nome do meu filho é: {nome.upper()+ '!'*3}')

import math 

x= 0.5

print(f'cos de ({x}) = {math.cos(x)}')

dicionario= dict({'nome':'Daniel','ocupação':'Dev Backend'})

print(f'{dicionario['nome']} é um {dicionario['ocupação']}')

print (linha*28)

time = "SPFC"
titulo = "SuperCopa Rei"
rival = "Palmeiras"

print(
f"O {time} foi campeão"
f" Da {titulo}"
f" Enfrentando o Rival de estado {rival}"

)

