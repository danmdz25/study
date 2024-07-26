''' while {condição}:
   {código} '''


x = int(input("Selecione o primeiro número: "))
y = int(input("Selecione o segundo número: "))

somaDosValores= x+y

while True: 
    try:
        somaDoCliente=int(input("Insira a soma dos valores que você colocou: "))
        if somaDoCliente==somaDosValores:
            print("Parabéns! você acertou")
            break
        else:
            print("Você errou. tente novamente.")
    except ValueError: 
        print("Por favor, insira um numero válido.")