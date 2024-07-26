#FAÇA UM PROGRAMA QUE CONFIRME A SENHA:
#SENHA: 1234
# CASO A SENHA ESTEJA ERRADA : ACESSO NEGADO	
# CASO A SENHA ESTEJA CERTO: ACESSO	PERMITIDO

senha= 1234

solicitacaoSenha= int(input("Insira aqui a senha: "))

if solicitacaoSenha ==senha: 
    print("ACESSO PERMITIDO")
else: print("ACESSO NEGADO")