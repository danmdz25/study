class loja:
  def __init__(self, nome, endereco, telefone, produtos):
    self.nome = nome
    self.endereco = endereco
    self.telefone = telefone
    self.produtos = produtos

  def listar_produtos(self):
    for produto in self.produtos:
      print(f"Nós vendemos:{produto}")

  def __str__(self):
    return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"



name = input('Insira o nome da sua loja: ')
adress = input('Insira o endereço da sua loja: ')
phone = input('Insira o telefone da sua loja: ')
noList=['não','not','no','n','nao']
products = []
while True:
  product = input('Insira um produto que você vende: ')
  products.append(product)
  quest = input('Deseja adicionar mais algum produto? (S/N): ')
  if quest in (noList):
    break
loja_1 = loja(name, adress, phone, products)
loja_1.listar_produtos()


print(loja_1.nome)
print(loja_1)