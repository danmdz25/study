#  faça um programa que realize a tabuada de qualquer número inteiro 
# do 1 ao 10

numero= int(input('Insira aqui o número que deseja ver a taboada do 1 ao 10: : '))

taboada= 1

print(f'Taboada do {numero} ')

while taboada< 10:
    print(f'{numero} X {taboada} = {numero*taboada} ')
    taboada+=1

    