lista = [1,2,3,4,5]

for item in lista: print(item)

listaDeNomes= ['Daniel','Anna', 'Eloise','Denise', 'Deyse']

for nomes in listaDeNomes: 
 if nomes == 'Eloise': break
 else: print(nomes)

print( '-'*28)
 
for nomes in listaDeNomes: 
  if nomes == 'Deyse': continue
  else: print(nomes)

print( '-'*28)
  
for nomes in listaDeNomes: 
 if nomes == 'Josué': break
 else: print("O nome josué não foi encontrado")