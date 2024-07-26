#FAÇA UM APP QUE REGISTRE O PESO IDEAL, BASEADO NA ALTURA E O SEXO DA PESSOA.
# 1 - MULHER 
# 2 - HOMEM 
# para	mulheres:	(62.1	*	Altura)	– 44.7	
# para	homens:	(72.7	*	Altura)	– 58	


sexo= int(input("Insira aqui o seu sexo, 1 caso seja mulher, 2 caso seja homem: "))
altura = float(input("Insira aqui sua altura em centimetros: "))


if sexo == 1: 
    print((f"Você se identifica como mulher  e seu peso ideal é: {(altura*62.1)-44.7} "))
else: print((f"Você se identifica como homem  e seu peso ideal é: {(altura*72.7)-58} "))