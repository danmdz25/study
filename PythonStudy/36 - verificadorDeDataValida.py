# Anos bissextos são aqueles que são múltiplos de 4, como 1996, 2000, 2004, etc. (ou seja, podem ser divididos por 4 sem deixar resto).
# No entanto, há uma exceção: anos múltiplos de 100 que não são múltiplos de 400 não são bissextos.
# Portanto, temos duas condições para verificar se um ano é bissexto:
# Condição 1: O ano deve ser múltiplo de 4 e não ser múltiplo de 100.
# Condição 2: O ano deve ser múltiplo de 400 (se for múltiplo de 400, automaticamente é múltiplo de 4).

ano = int(input('Digite um ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('É um ano bissexto.')
else:
    print('Não é um ano bissexto.')
