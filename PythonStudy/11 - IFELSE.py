idade = int(input("Qual a sua idade?"))
temCartao= True if idade >= 18 else False

if idade >=18:
    if temCartao: print("Você pode comprar")
    else: print("Você não tem um cartão")
else: print("você é menor de idade")