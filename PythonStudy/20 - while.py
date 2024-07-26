import random 
numeroMagico= random.randint(0,10)
tentativas = 0
while tentativas<3:
        numero=int(input("Insira aqui um número(0 até 100): "))
        if numero==numeroMagico:
            print("Parabéns! você acertou")
            break
        tentativas+=1
else:
            print(f"Você errou. Boa sorte na próxima, o número era: {numeroMagico}")
   