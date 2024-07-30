import math
lambdaList=[1,2,3,4,5,6,7,8,9,10]
quadLamb=lambda x: x**2
quadrado = list(map(quadLamb,lambdaList))
radLamb=lambda x: math.sqrt(x)
for item in quadrado:
  print(item)
  print('--------')
  print(radLamb(item))
  print('--------')
