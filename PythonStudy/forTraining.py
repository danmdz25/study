print('exercicio 1')
print('')
supermarketList=['banana','apple','orange','pineapple','kiwi','melon','grapes','pear','watermelon','strawberry']

for item in supermarketList:
  print(item)

print('')
print('exercicio 2')

start=2
end=22
for i in range(start,end+1):
  print(i)
print('')
print('exercicio 3')

for i in range(0,21):
  if i%2==0:
    print(i)
print('')
print('exercicio 4')

soma=0
contador=0
for i in range(0,101):

  if i%2!=0 and i%3==0:
    print(f'O número {i} é impar')
    soma+=i
    contador+=1
print(f'Ao final tivemos {contador} números impares e a soma deles é {soma}')