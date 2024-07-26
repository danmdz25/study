valorGanhoPorHora= float(input("insira aqui o valor referente ao quanto você recebe por hora: "))
horasTrabalhadas= int(input("insira aqui a quantidade de horas que você trabalha por dia: "))
diasTrabalhados= int(input("insira aqui quantos dias por mês você trabalha: "))
horasTrabalhadasMes= (horasTrabalhadas*diasTrabalhados)
salario=valorGanhoPorHora*horasTrabalhadasMes
print("O seu salário, sem os reajustes, ficará no valor de: ", salario)