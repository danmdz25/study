lojas = ['Rio de Janeiro','São Paulo', 'Curitiba']
vendas = [10000, 20000, 50000]
resultados= []

for i in range(3):
   tupla=(lojas[i],vendas[i])
   resultados.append(tupla)
print(resultados)
print(resultados[1][0])