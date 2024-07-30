print('bem vindo ao melhor jogo de estudo de taboada do mundo')
print('vamos começar')
table = lambda x,y: x*y

numeroTaboada = int(input("Qual número você quer estudar: "))
pontos=0
for i in range(1,11):
  resolucao=table(numeroTaboada,i)
  print('Qual o resultado da conta abaixo?')
  resposta=int(input(f'{numeroTaboada} x {i} = '))
  if resposta == resolucao:
    print('você acertou')
    pontos+=1
    if pontos==10:
      print('Parabéns você acertou todas as contas')
        
  else:
    print('voce errou')
    print(f'O valor correto era: {resolucao}')
    break
