pares = [(x, y,z) for x in range(3) for y in range(1,3) for z in range (3) if x + y + z < 3 and y>0]
print(pares)  