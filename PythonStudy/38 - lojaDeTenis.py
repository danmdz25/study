#Faça uma loja de tenis, que pergunte qual marca o cliente quer
# Qual número ele calça e verificar se há disponibilidade
# 
print("Bem-vindo a loja de tênis!")
print("Escolha uma das nossas opções e na sequencia o numero do seu calçado:")
print("1. Tenis Nike")
print("2. Tenis Adidas")
print("3. Tenis Vans")

escolha = int(input("Digite o número da opção desejada: "))
numero = int(input("Digite o número: "))

loja = {
1:'Nike',
2:'Adidas',
3:'Vans'
}

tenisNike = [37,38,39,40,41,42,43]
tenisAdidas = [37,38,39,40,41]
tenisVans = [36,37,38,39,40,41,43]

print()
if escolha == 1 and numero in tenisNike: 
    print(f"Você comprou um tenis da : {loja[escolha]}")
elif escolha ==1 and numero not in tenisNike:
    print(f"Não temos esse número disponivel para a marca escolhida que foi a: {loja[escolha]}")
elif escolha == 2 and numero in tenisAdidas:
    print(f"Você comprou um tenis da: {loja[escolha]} ")
elif escolha ==2 and numero not in tenisAdidas:
    print(f"Não temos esse número disponivel para a marca escolhida que foi a: {loja[escolha]}")
elif escolha ==3 and numero in tenisVans:
    print(f"Você comprou um tênis da marca: {loja[escolha]}")
elif escolha == 3 and numero not in tenisVans:
    print(f"Não temos esse número disponivel para a marca escolhida que foi a: {loja[escolha]} ")




