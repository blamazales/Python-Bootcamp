# Cálculo de Salário Líquido (IR)

salario_bruto = float(input("Informe o salário bruto: R$ "))

if salario_bruto <= 1903.98:
    aliquota = 0
elif salario_bruto <= 2826.65:
    aliquota = 7.5
elif salario_bruto <= 3751.05:
    aliquota = 15
elif salario_bruto <= 4664.68:
    aliquota = 22.5
else:
    aliquota = 27.5

imposto = salario_bruto * (aliquota / 100)
salario_liquido = salario_bruto - imposto

print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
print(f"Alíquota aplicada: {aliquota}%")
print(f"Imposto de Renda: R$ {imposto:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")