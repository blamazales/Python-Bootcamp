# Três Números em Ordem Crescente

numeros = []
for i in range(3):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))

numeros.sort()
print(f"Ordem crescente: {numeros}")