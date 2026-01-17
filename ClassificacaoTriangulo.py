# Classificação de Triângulos

a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

if a == b == c:
    print("Triângulo Equilátero")
elif a == b or a == c or b == c:
    print("Triângulo Isósceles")
else:
    print("Triângulo Escaleno")