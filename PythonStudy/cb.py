class Chabot:
  def __init__(self,intent,entities,response,context):
      self.intent=intent
      self.entities=entities
      self.response=response
      self.context=context
print('Olá, seja bem vindo(a) ao Suporte TiraSenha!')
print('Caso esteja com duvida, nós vamos te ajudar! Qual dos modelos de painel abaixo mais se enquadra no seu?🤔')
A_25='A-25'
A_60='A-60'
A_625='A-625'
LT_60='LT-60'
LT_625='LT-625'
IDK='Não sei'


# print('')

# print(f'''
# {A_25}
# {A_60}
# {A_625}
# {LT_60}
# {LT_625}
# {IDK}
# ''')

# resposta_bv= input(f'Digite o modelo do painel que é o seu: ')
# def sup_agilize(resp):
#   print(f'aqui esta o suporte para o seu {resp}')
# def sup_ledtime(resp):
#   print(f'aqui esta o suporte para o seu {resp}')
# while True:
#   if resposta_bv.lower() == A_25.lower():
#     sup_agilize(resposta_bv)
#     intent='agilize_sup'
#     break
#   elif resposta_bv.lower() == A_60.lower():
#     sup_agilize(resposta_bv)
#     intent='agilize_sup'
#     break
#   elif resposta_bv.lower() == A_625.lower():
#     sup_agilize(resposta_bv)
#     intent='agilize_sup'
#     break
#   elif resposta_bv.lower() == LT_60.lower():
#     sup_ledtime(resposta_bv)
#     intent='ledtime_sup'
#     break
#   elif resposta_bv.lower() == LT_625.lower():
#     sup_ledtime(resposta_bv)
#     intent='ledtime_sup'
#     break
#   elif resposta_bv.lower() == IDK.lower():
#     print(resposta_bv.lower())
#     intent='idk_1'
#     break
#   else:
#     print('Não entendi, por favor tente novamente!')
#     resposta_bv= input(f'Digite novamente o modelo do seu painel: ')



