while True:
    nota = int(input("Digite uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        print("Nota válida:", nota)
        break
    else:
        print("Nota inválida. Tente novamente.")
