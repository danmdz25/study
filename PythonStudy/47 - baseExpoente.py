# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem.


base= int(input('Insira aqui o valor da sua base: '))
expoente = int(input('Insira aqui o valor do seu expoente: '))
resultado = 1
for _ in range(expoente):
    resultado *= base

print(f'O valor de {base} elevado a {expoente} é {resultado}')
