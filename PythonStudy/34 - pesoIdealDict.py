#FAÇA UM APP QUE REGISTRE O PESO IDEAL, BASEADO NA ALTURA E O SEXO DA PESSOA.
# 1 - MULHER 
# 2 - HOMEM 
# para	mulheres:	(62.1	*	Altura)	– 44.7	
# para	homens:	(72.7	*	Altura)	– 58	

sexo= int(input("Insira aqui o seu sexo, 1 caso seja mulher, 2 caso seja homem: "))
altura = float(input("Insira aqui sua altura em centimetros: "))


genero = {
1:'Mulher',
2:'Homem'
}
def formulaHomem(altura):
    return 72.7 * altura - 58
def  formulaMulher(altura):
    return 62.1 * altura - 44.7

formula = {
1: formulaMulher(altura),
2: formulaHomem(altura)
}

print(f"Você se identifica como {genero[sexo]} e seu peso ideal é: {formula[sexo]}")
