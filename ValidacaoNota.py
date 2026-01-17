# Validação de Nota com Repetição

while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        print("Nota válida. Obrigado!")
        break
    else:
        print("Valor inválido! Tente novamente.")