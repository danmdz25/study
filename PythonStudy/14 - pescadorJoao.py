#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
#deve pagar uma multa de R$ 4,00 por quilo excedente. 
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
#Imprima os dados do programa com as mensagens adequadas.


peso= float(input("Insira aqui a quantidade, em kg, de peixes que você pegou: "))

pesoMaximo= 50
multaPorKg= 4.00

pesoMinimo= 10
ajudaPorFaltaDePeixe= 10.00

excesso = max(0,peso-pesoMaximo)
multa= excesso * multaPorKg

deficienciaNaPesca= max(0,pesoMinimo-peso)
suporte= deficienciaNaPesca*ajudaPorFaltaDePeixe
#def serve para definir uma função
#A sintaxe de uma função é definida por três partes: 
#nome, parâmetros e corpo, o qual agrupa uma sequência de linhas que representa algum comportamento
def excessoDePeso(excesso, multa):
    print(f"Excesso de peso {excesso} kg")
    print(f"Valor da multa {multa:.2f}R$")
#def serve para definir uma função
def escassezDePeso(deficienciaNaPesca, suporte):
  print(f"Falta de pesca {deficienciaNaPesca}kg")
  print(f"Valor da ajuda {suporte:.2f}R$")
 
if peso>50: excessoDePeso(excesso, multa)
elif peso<=10: escassezDePeso(deficienciaNaPesca, suporte)
else: print(f"Você pegou {peso}KG, ou seja uma quantidade boa de peixes porém não é excessiva! Parabéns!")
