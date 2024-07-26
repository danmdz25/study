listaDeCompras = ['banana','laranja','maçã']
print(listaDeCompras)

# #para adicionar um item na lista:  

listaDeCompras.append('PC Gamer')
listaDeCompras.insert(4,'uva')

# para remover um item da  lista:

del listaDeCompras[4]
listaDeCompras.remove('banana')

print(listaDeCompras)


listaSonhos=[]

item = listaDeCompras.pop(-1)
print (item)

listaSonhos.append(item)
print(listaSonhos)



# Criando lista de tarefas

tarefa= []
atividade = input("Coloque aqui uma de suas tarefas: ")

tarefa.append(atividade)

print(tarefa)



while atividade: 
    atividade = input("Coloque aqui uma de suas tarefas: ")
    tarefa.append(atividade)

    print(tarefa)
