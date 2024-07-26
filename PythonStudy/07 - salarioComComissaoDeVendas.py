#Salario com comissão de vendas, 0,05* do salario por venda
salario = float(input("Qual o seu salário mensal: "))
vendasNoMes= int(input("Quantas vendas você faz no mês? "))
comissao= (salario*vendasNoMes)*0.05
salarioComComissao= salario+comissao

print("O seu salário com as comissões inclusas ficam no valor de: ", salarioComComissao)