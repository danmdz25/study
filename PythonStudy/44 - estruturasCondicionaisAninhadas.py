# if condicao1: 
#       if condicao2:
#           print(“condicao1 e condicao2 são verdadeiras”

nota1= int(input("insira aqui sua nota 1: "))
nota2= int(input("insira aqui sua nota 2: "))
frequencia= float(input("Insira a sua frequencia: "))
media=(nota1+nota2)/2
if media >= 6: 
    if frequencia>=70:
        print(f'Sua media foi: {media} e sua frequencia foi {frequencia}, você passou de ano!')
else: print('você reprovou')