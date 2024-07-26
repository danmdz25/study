#faça um programa que verifique se é vogal ou consoante
letra = input("Digite aqui uma letra: ")

vogal = ['a', 'e', 'i', 'o', 'u']
consoante = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

def digitouVogal(letra):
    return f"Você digitou {letra}, e isso é uma vogal"

def digitouConsoante(letra):
    return f'Você digitou {letra} e isso é uma consoante'

if letra.lower() in vogal:
    print(digitouVogal(letra))
elif letra.lower() in consoante:
    print(digitouConsoante(letra))
else:
    print("Você não digitou uma letra válida!")

