class Pessoa:
  def __init__(self,nome=None,idade=None):
    self.nome=nome
    self.idade=idade
    
  @classmethod
  def criar_de_data_nascimento(cls, ano, mes, dia, nome):
    idade= 2024-ano
    return Pessoa(nome,idade)
    
  @staticmethod
  def e_maior_idade(idade):
    return idade >= 18

# p = Pessoa('Daniel',18)
# print(p.nome,p.idade)

p=Pessoa.criar_de_data_nascimento(2006,1,25,'Daniel')
print(p.nome,p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))