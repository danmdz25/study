class bicicleta:
  # self é referencia explicita do objeto, representa a instancia do objeto
  def __init__(self, cor, modelo, ano, valor):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.valor = valor

  def buzinar(self):
    print('BeeeBeep')

  def andar(self, correr=False, parar=True):
    self.correr = correr
    self.parar = parar

  def __str__(self):
    return   f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


bike_1 = bicicleta('Vermelha', 'caloi', '2020', 'R$2.000,00')
bike_1.buzinar()
bike_1.parar = True
if bike_1.parar:
  print('Parando a Bike')
  print('Bike parada')
else:
  print('Vrummm')
print(bike_1.cor)
print(bike_1.modelo)
print(bike_1.ano)
print(bike_1.valor)

print(bike_1)
