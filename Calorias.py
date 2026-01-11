# 8. Calorias Queimadas no Mês

horas_semana = float(input("Quantas horas de exercício você faz por semana? "))

# 1 hora = 60 minutos
# 1 mês aproximado = 4 semanas
minutos_mes = horas_semana * 60 * 4
total_calorias = minutos_mes * 5

print(f"Em um mês, você queima aproximadamente {total_calorias:.0f} calorias.")