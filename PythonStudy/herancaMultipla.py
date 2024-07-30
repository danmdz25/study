class Animal:
  def __init__(self,nro_patas):
    self.nro_patas = nro_patas
    
  def __str__(self):
    className=self.__class__.__name__
    return f"{className}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
  def __init__(self,cor_pelo,**kw):
    self.cor_pelo=cor_pelo
    super().__init__(**kw)

  
class Ave(Animal):
  def __init__(self,cor_bico,**kw):
    self.cor_bico=cor_bico
    super().__init__(**kw)
    
class FalarMixin:
  def falar(self):
    return 'oi estou falando'

class Gato(Mamifero,FalarMixin):
  pass

class Cao(Mamifero,FalarMixin):
  def __init__(self,raca,cor_pelo,nro_patas):
    super().__init__(cor_pelo=cor_pelo,nro_patas=nro_patas)
    self.raca=raca


class Ornitorrinco(Mamifero,Ave,FalarMixin):
  def __init__(self,cor_bico,cor_pelo,nro_patas):
    # print(Ornitorrinco.__mro__)
    super().__init__(cor_pelo=cor_pelo,cor_bico=cor_bico, nro_patas=nro_patas)

  
    

gato= Gato(nro_patas=4,cor_pelo='preto')
ornitorrinco= Ornitorrinco(nro_patas=2,cor_pelo='verde',cor_bico='amarelo')
cao = Cao(nro_patas=4,cor_pelo='preto',raca='Rottweiler')


animalsList=[gato,ornitorrinco,cao]

for animal in animalsList:
  print(animal)

# print(ornitorrinco)

