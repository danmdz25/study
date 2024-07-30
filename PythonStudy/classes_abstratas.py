from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):

  @abstractmethod
  def ligar(self):
    pass

  @abstractmethod
  def desligar(self):
    pass

  @property
  @abstractproperty
  def marca(self):
    pass


class ControleTV(ControleRemoto):

  def ligar(self):
    print('Ligando a TV...')
    print('Ligada')

  def desligar(self):
    print('Desligando a TV...')
    print('Desligada!')

  @property
  def marca(self):
    return 'Philco'


class ControleArCondicionado(ControleRemoto):

  def ligar(self):
    print('Ligando o Ar Condionado...')
    print('Ligado!')

  def desligar(self):
    print('Desligando o Ar Condionado...')
    print('Desligada!')

  @property
  def marca(self):
    return 'LG'


controle = ControleTV()
controle_2 = ControleArCondicionado()

controle.ligar()
controle.desligar()
controle_2.ligar()
controle_2.desligar()
print(controle.marca)
print(controle_2.marca)
