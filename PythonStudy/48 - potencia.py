# Solicite a base e o expoente do usuário
base = int(input('Insira aqui o valor da sua base: '))
expoente = int(input('Insira aqui o valor do seu expoente: '))

# Calcule a potência usando a função pow
resultado = pow(base, expoente)

# Imprima o resultado
print(f'O valor de {base} elevado a {expoente} é {resultado}')
