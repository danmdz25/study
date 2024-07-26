
paisA=int(input("Insira aqui a população do país A: "))
paisB=int(input("Insira aqui a população do país B: "))

anos = 0

while paisA < paisB:
    anos += 1
    paisA += paisA * .03
    paisB += paisB * .015

print(f"A população do país A: {paisA:.0f}, ultrapassou a do pais B: {paisB:.0f}, em {anos} anos")
