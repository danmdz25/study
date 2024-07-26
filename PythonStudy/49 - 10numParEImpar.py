# Faça um programa que peça 10 números inteiros, 
# calcule e mostre a quantidade de números pares e 
# a quantidade de números impares.


n1= int(input("Insira aqui um numero: "))
n2= int(input("Insira aqui um numero: "))
n3= int(input("Insira aqui um numero: "))
n4= int(input("Insira aqui um numero: "))
n5= int(input("Insira aqui um numero: "))
n6= int(input("Insira aqui um numero: "))
n7= int(input("Insira aqui um numero: "))
n8= int(input("Insira aqui um numero: "))
n9= int(input("Insira aqui um numero: "))
n10= int(input("Insira aqui um numero: "))


numeros= [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]
numeroTamanhoDaLista= len(numeros)
numerosPares=[]
numerosImpares=[]


for numero in numeros :
    if numero % 2 == 0:
        numerosPares.append(numero)
    else: 
        numerosImpares.append(numero)

print(f'Quantidade de números pares: {len(numerosPares)}')
print(f'Quantidade de números ímpares: {len(numerosImpares)}')

print(f'Números pares: {numerosPares}')
print(f'Números ímpares: {numerosImpares}')
        