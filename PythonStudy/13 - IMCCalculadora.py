##IMC = peso/(altura x altura)
##IMC <18,5kg/m2 - baixo peso.
##IMC >18,5 até 24,9kg/m2 - eutrofia (peso adequado)
##IMC ≥25 até 29,9kg/m2 - sobrepeso. 
##IMC >30,0kg/m2 até 34,9kg/m2 - obesidade grau 1.
##IMC > 35,0kg/m2 até 39,9 kg/m2 - obesidade grau 2.
##IMC > 40,0kg/m2 ou mais - obesidade mórbida


peso= float(input("Qual o seu peso: "))
altura= float(input("Qual o sua altura (em centimetros): "))
imc = round((peso /(altura*altura)* 10000),2)

if imc<= 18.5 : print("O seu indice de massa corporal é de: ",imc, " isso é considerado baixo peso.")
elif imc>18.5 and imc<=24.9: print("O seu indice de massa corporal é de: ",imc," isso é considerado eutrofia (peso adequado)")
elif imc>25.0 and imc<=29.9: print("O seu indice de massa corporal é de: ",imc," isso é considerado sobrepeso ")
elif imc>30.0 and imc <=34.9:print("O seu indice de massa corporal é de: ",imc," isso é considerado obesidade de grau 1")
elif imc>35.0 and imc <=39.9:print("O seu indice de massa corporal é de: ",imc," isso é considerado obesidade de grau 2")
elif imc>40:print("O seu indice de massa corporal é de: ",imc," isso é considerado obesidade mórbida")

