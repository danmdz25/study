class Gato:
  def __init__(self,nome,cor,acordado=True):
    self.nome=nome
    self.cor=cor
    self.acordado=acordado
  
  def __del__(self):
    print('removendo a instancia da classe')
  def miar(self):
    print('miau')




g = Gato('Felix','preto')
g.miar()
del g
