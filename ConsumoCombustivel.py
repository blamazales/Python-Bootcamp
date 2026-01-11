# 4. Consumo Médio de Combustível

distancia = float(input("Digite a distância percorrida (km): "))
litros = float(input("Digite a quantidade de litros consumidos: "))

if litros > 0:
    consumo_medio = distancia / litros
    print(f"O consumo médio do seu veículo é de {consumo_medio:.2f} km/l.")
else:
    print("A quantidade de litros deve ser maior que zero.")