# Faça um programa que leia um nome de usuário e a sua senha.
# e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario=input("Insira aqui o seu usuário: ")
senha= input("Insira aqui a sua senha: ")
while True:
    if usuario != senha:    
        print("Você criou o seu cadastro!!")
        break
    else: 
        print("Você não pode utilizar a senha igual ao seu nome!")