class automovel:

  def __init__(self, marca, modelo, cor, preco, radio, ar_condicionado,
               combustivel, placa, ano, cambio, qtd_rodas):
    self.marca = marca
    self.modelo = modelo
    self.cor = cor
    self.preco = preco
    self.radio = radio
    self.ar_condicionado = ar_condicionado
    self.combustivel = combustivel
    self.placa = placa
    self.ano = ano
    self.cambio = cambio
    self.qtd_rodas = qtd_rodas

  def ligar_motor(self):
    print('ligando motor')

  def __str__(self):
    return f'{self.__class__.__name__}: {", ".join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}'


class Carro(automovel):
  pass


class Moto(automovel):
  pass


carro = Carro(marca='Chevrolet',
              modelo='S10',
              cor='Preto',
              preco=218000,
              radio=True,
              ar_condicionado=True,
              combustivel='Diesel',
              placa='ABC1234',
              ano=2025,
              cambio='Automatico',
              qtd_rodas=4)

moto = automovel(marca='Yamaha',
                 modelo='R1',
                 cor='Branco',
                 preco=120000,
                 radio=False,
                 ar_condicionado=False,
                 combustivel='Alcool',
                 placa='DEF5678',
                 ano=2023,
                 cambio='Manual',
                 qtd_rodas=2)

automoveis = [carro, moto]
for autos in automoveis:
  print(
      f"""Meu automovel{' é uma moto'if autos.qtd_rodas==2 else ' é um carro'} da {autos.marca}, um {autos.modelo} de {autos.ano} {"com" if autos.ar_condicionado else "sem"} ar condicionado e {"com" if autos.radio else "sem"} rádio, ele usa {autos.combustivel} e sua placa é {autos.placa}, paguei R${autos.preco} nele"""
  )
