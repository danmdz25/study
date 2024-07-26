#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%)

valorGanhoPorHora= float(input("insira aqui o valor referente ao quanto você recebe por hora: "))
horasTrabalhadas= int(input("insira aqui a quantidade de horas que você trabalha por dia: "))
diasTrabalhados= int(input("insira aqui quantos dias por mês você trabalha: "))
horasTrabalhadasMes= (horasTrabalhadas*diasTrabalhados)
salario=valorGanhoPorHora*horasTrabalhadasMes
descontoIR= salario*0.11
descontoINSS= salario*0.08
descontoSindicato= salario*0.05
salarioLiquido= salario-(descontoINSS+descontoIR+descontoSindicato)
print("O seu salário, sem reajustes, ficará no valor de: R$", salario,)
print("O valor descontado referente ao importo de renda é de: R$", descontoIR, )
print("O valor descontado referente ao INSS é de: R$", descontoINSS, )
print("O valor descontado referente ao Sindicato é de: R$", descontoSindicato, )
print("O seu salário, com os reajustes, ficará no valor de: R$", salarioLiquido,)


