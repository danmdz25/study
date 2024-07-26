#ESCREVA UM PROGRAMA QUE IRÁ LER 3 NÚMEROS INTEIROS 
# E IRÁ COLOCALOS DE FORMA CRESCENTE



numero1=int(input("insira o primeiro número aqui:  "))
numero2=int(input("insira o primeiro número aqui:  "))
numero3=int(input("insira o primeiro número aqui:  "))


numeros=[numero1,numero2,numero3]
numeros.sort()
print (f'Você escolheu os números: {numero1}, {numero2} e {numero3}, em ordem crescente eles ficam assim: {numeros}')
