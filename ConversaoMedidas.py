3. Faça  um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.

km = float(input("Digite a quantidade de quilômetros: "))

metros = km * 1000
centimetros = km * 100000
milimetros = km * 1000000

print(f"{km}km equivalem a:")
print(f"- {metros:.0f} metros")
print(f"- {centimetros:.0f} centímetros")
print(f"- {milimetros:.0f} milímetros")