# Investigação Crime

perguntas = [
    "Telefonou para a vítima? ",
    "Esteve no local do crime? ",
    "Mora perto da vítima? ",
    "Devia para a vítima? ",
    "Já trabalhou com a vítima? "
]

respostas_positivas = 0

for p in perguntas:
    resp = input(p + "(s/n): ").lower()
    if resp == 's':
        respostas_positivas += 1

if respostas_positivas == 5:
    print("Classificação: Assassino")
elif respostas_positivas >= 3:
    print("Classificação: Cúmplice")
elif respostas_positivas == 2:
    print("Classificação: Suspeita")
else:
    print("Classificação: Inocente")