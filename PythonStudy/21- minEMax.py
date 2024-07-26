# . Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.
numero1 = int(input("Escolha o seu Primeiro número: "))
numero2 = int(input("Escolha o seu Segundo número: "))
numero3 = int(input("Escolha o seu Terceiro número: "))

maiorNumero= max(numero1,numero2,numero3)
menorNumero= min(numero1,numero2,numero3)

print(f"Dos números que você escolheu,({numero1}, {numero2}, {numero3}), o maior é o : {maiorNumero}")
print(f"Dos números que você escolheu,({numero1}, {numero2}, {numero3}), o menor é o : {menorNumero}")

