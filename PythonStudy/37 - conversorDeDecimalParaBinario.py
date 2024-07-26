print("Bem-vindo ao Conversor de Bases Numéricas!")
print("Escolha a base de origem:")
print("1. Octal")
print("2. Decimal")
print("3. Hexadecimal")
    
escolha = int(input("Digite o número da opção desejada: "))
numero = input("Digite o número: ")

if escolha == 1:
        decimal = int(numero, 8)
elif escolha == 2:
        decimal = int(numero)
elif escolha == 3:
        decimal = int(numero, 16)
else:
    print("Opção inválida. Escolha 1, 2, 3 ou 4.")

print("O número decimal correspondente é:", decimal)
print("Em binário:", bin(decimal)[2:])  # Removendo o prefixo "0b"
print("Em octal:", oct(decimal)[2:])  # Removendo o prefixo "0o"
print("Em hexadecimal:", hex(decimal)[2:])  # Removendo o prefixo "0x"

