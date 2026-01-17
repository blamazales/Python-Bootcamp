# Contador de Pares e Ímpares (Positivos)

pares = 0
impares = 0

while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    if num < 0:
        print("Apenas números positivos são contados.")
        continue
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")