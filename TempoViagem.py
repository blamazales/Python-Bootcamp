# 5.Comparativo de Tempo de Viagem

distancia = float(input("Digite a distância da viagem em quilômetros: "))

# Velocidades definidas
vel_aviao = 600
vel_carro = 100
vel_onibus = 80

# Cálculos
tempo_aviao = distancia / vel_aviao
tempo_carro = distancia / vel_carro
tempo_onibus = distancia / vel_onibus

print(f"\nPara percorrer {distancia}km, o tempo estimado é:")
print(f"- Avião: {tempo_aviao:.2f} horas")
print(f"- Carro: {tempo_carro:.2f} horas")
print(f"- Ônibus: {tempo_onibus:.2f} horas")