# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

sexoConfirmacao= ["f","m"]
relacionamento= ["c","s","v","d"]
sexoDict= {
    'f':"femino",
    'm':"homem"
}
estadoCivilDict={
    's':'solteiro',
    'c':'casado',
    'd':'divorciado',
    'v':'viuvo'
}
while True:

    nome=input("Insira aqui o seu nome: ")    
    idade=int(input("Insira aqui sua idade: "))
    salario= float(input("Insira aqui o seu salário: "))
    sexo= input("Insira o seu sexo, f para feminino e m para masculino: ")
    estadoCivil= input("Insira o seu estado civil, s para solteiro, c para casado, v para viuvo e d para divorciado: ")
    
    if len(nome) > 3 and 0 <= idade <= 150 and salario > 0 and sexo in sexoConfirmacao and estadoCivil in relacionamento:
        print(f'''Você teve todos os seus dados verificados, seus dados são: 
          nome: {nome} 
          idade: {idade} 
          salario: R${salario}  
          sexo: {sexoDict[sexo]}  
          estado cívil: {estadoCivilDict[estadoCivil]}''')
        break 
    else: 
        print("Algum dos seus dados está invalido, tente novamente.")



    