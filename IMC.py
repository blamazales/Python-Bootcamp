# 6. Cálculo de IMC

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

# Dica extra: Verificação básica
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
else:
    print("Classificação: Acima do peso")