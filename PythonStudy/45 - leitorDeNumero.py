# Faça um programa que leia 5 números 
# e informe a soma e a média dos números.

n1=int(input("Insira aqui o primeiro número: "))
n2=int(input("Insira aqui o segundo número: "))
n3=int(input("Insira aqui o terceiro número: "))
n4=int(input("Insira aqui o quarto número: "))
n5=int(input("Insira aqui o quinto número: "))

numeros= []

numeros.append(n1)
numeros.append(n2)
numeros.append(n3)
numeros.append(n4)
numeros.append(n5)

maiorNumero= max(numeros)
soma = sum(numeros)
media = soma / len(numeros)

for numero in numeros:
    print(f'Os números que você escolheu: {numero}')


print(f'A soma dos números que você escolheu é: {soma}')
print(f'A média dos números que você escolheu é: {media}')

  

    