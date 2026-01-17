# Resolver Erro
def calcular_media(valores):
    # Verificamos se a lista não está vazia para evitar divisão por zero
    if not valores:
        return 0
    
    soma = 0.0
    for valor in valores:
        soma += valor
    
    # O tamanho deve ser a quantidade real de itens na lista
    tamanho = len(valores)
    media = soma / tamanho
    return media

continuar = True
valores = []

while continuar:
    entrada = input('Digite um número ou "ok" para calcular: ')
    
    if entrada.lower() == 'ok':
        continuar = False
    else:
        try:
            # Converte a entrada para número e adiciona na lista
            numero = float(entrada)
            valores.append(numero)
        except ValueError:
            print("Por favor, digite um número válido ou 'ok'.")

# Chama a função e armazena o resultado
resultado_media = calcular_media(valores)

print('A média calculada para os valores {} foi de {:.2f}'.format(valores, resultado_media))