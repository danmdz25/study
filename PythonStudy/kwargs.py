def info (**informacoes):
  for chave, valor in informacoes.items():
    print(f'{chave} é {valor}')

info(nome='Daniel', idade=18, cidade='São Paulo')