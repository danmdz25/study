# Inicializa os dois primeiros números da sequência
a, b = 0, 1

# Imprime os dois primeiros números da sequência
print(a)
print(b)

# Enquanto o último número calculado for menor ou igual a 500
while b <= 500:
    # Calcula o próximo número da sequência
    c = a + b
    # Atualiza os valores de a e b para os próximos cálculos
    a, b = b, c
    # Imprime o próximo número da sequência
    print(c)
