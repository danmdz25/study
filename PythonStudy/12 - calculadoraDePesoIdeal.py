#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
#usando a seguinte fórmula: (72.7*altura) - 58
#testar adaptação que n necessariamente obrigue a colocar em metros


altura = float(input("Qual a sua altura em metros: "))
pesoIdeal= (72.7*altura)-58

print("O seu peso ideal é: ",pesoIdeal)
