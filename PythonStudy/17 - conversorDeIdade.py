#Desenvolver um app que converta anos em meses e dias
# Mes - 30 
# Dias - 365

idade= int(input("Insira sua idade: "))

conversorIdadeMes= idade*12
conversorIdadeDias= idade*365

print(f'Você tem {idade} anos de idade, sua idade em meses é de: {conversorIdadeMes}, já sua idade em dias é: {conversorIdadeDias}')