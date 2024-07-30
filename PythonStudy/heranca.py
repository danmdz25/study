class Veiculo:

  def __init__(self, cor, placa, numero_rodas):
    self.cor = cor
    self.placa = placa
    self.numero_rodas = numero_rodas

  def ligar_motor(self):
    print('ligando motor')

  def __str__(self):
    return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
  pass


class Carro(Veiculo):
  pass


class Caminhao(Veiculo):

  def __init__(self, carregado, cor, placa, numero_rodas):
    super().__init__(cor, placa, numero_rodas)
    self.carregado = carregado

  def esta_carregado(self):
    print(f"{'Sim'if self.carregado else 'Não'} estou carregado")


moto = Motocicleta(cor='vermelha', placa='ABC1234', numero_rodas=2)
moto.ligar_motor()

carro = Carro(cor='azul', placa='DEF5678', numero_rodas=4)
carro.ligar_motor()

caminhao = Caminhao(cor='preto',
                    placa='JED1234',
                    numero_rodas=8,
                    carregado=True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)
print(carro)
print(moto)
