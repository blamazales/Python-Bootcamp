# Execução das Instâncias

# 4. Crie uma instância da classe carro
meu_carro = Carro(cor="Prata", modelo="Sedan")

# 5. Faça o carro "andar" (Ligar e Acelerar)
print("--- Fazendo o carro andar ---")
meu_carro.liga()
meu_carro.acelera(50)
meu_carro.acelera(20)

# 6. Faça o carro "parar" (Desacelerar e Desligar)
print("\n--- Fazendo o carro parar ---")
meu_carro.desacelerar(70) # Reduzindo até parar
meu_carro.desliga()