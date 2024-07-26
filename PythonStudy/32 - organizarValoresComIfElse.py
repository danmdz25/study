#ESCREVA UM PROGRAMA QUE IRÁ LER 3 NÚMEROS INTEIROS 
# E IRÁ COLOCALOS DE FORMA CRESCENTE



n1=int(input("insira o primeiro número aqui:  "))
n2=int(input("insira o primeiro número aqui:  "))
n3=int(input("insira o primeiro número aqui:  "))




if n1<n2<n3:
    print(F'Os seus numeros em ordem crescente ficarão assim: {n1,n2,n3}')
elif n1<n3<n2:
    print(F'Os seus numeros em ordem crescente ficarão assim: {n1,n3,n2}')
elif n2<n1<n3:
    print(F'Os seus numeros em ordem crescente ficarão assim: {n2,n1,n3}')
elif n2<n3<n1:
    print(F'Os seus numeros em ordem crescente ficarão assim: {n2,n3,n1}')
elif n3<n1<n2:
    print(F'Os seus numeros em ordem crescente ficarão assim: {n3,n1,n2}')
else:
    print(F'Os seus numeros em ordem crescente ficarão assim: {n3,n2,n1}')