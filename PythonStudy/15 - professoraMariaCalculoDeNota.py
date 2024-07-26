#Maria é uma professora e ela precisa calcular as notas finais de seus alunos. 
#Cada aluno tem três notas: a nota do primeiro semestre, a nota do segundo semestre e a nota do exame final. 
#A nota final de cada aluno é calculada da seguinte maneira:
#A nota do primeiro semestre tem peso 2.
#A nota do segundo semestre tem peso 3.
#A nota do exame final tem peso 5.
#Portanto, a nota final é a média ponderada das três notas, onde os pesos são dados pelos números acima.
#Maria precisa que você faça um programa que leia as três notas de um aluno e calcule sua nota final. 
#O programa deve imprimir a nota final do aluno e uma mensagem indicando se o aluno foi aprovado ou reprovado. 
#Um aluno é aprovado se sua nota final for maior ou igual a 7, e reprovado caso contrário.

notaPrimeiroSemestre= float(input('Coloque a nota do seu primeiro semetre aqui: '))
notaSegundoSemestre= float(input('Coloque a nota do seu segundo semetre aqui: '))
notaExameFinal= float(input('Coloque a nota do seu exame final aqui: '))
pesoPrimeiroSemestre=2
pesoSegundoSemestre=3
pesoExameFinal=5

mediaFinal= ((notaPrimeiroSemestre*pesoPrimeiroSemestre)+ (notaSegundoSemestre*pesoSegundoSemestre)+(notaExameFinal*pesoExameFinal))/ (pesoPrimeiroSemestre+pesoSegundoSemestre+pesoExameFinal)

if mediaFinal>=7:
    print(f"Você foi aprovado!! parabéns, sua média final foi de {mediaFinal:.2f}")
elif mediaFinal>5.5 and mediaFinal<6.9: print(f"Você está de recuperação!!, sua média final foi de {mediaFinal:.2f}, na próxima se esforce mais!!")
else: print(f"Você foi reprovado, sua média final foi de {mediaFinal:.2f}, boa sorte no próximo ano. ")