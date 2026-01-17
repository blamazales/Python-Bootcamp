# Médias de 5 Alunos

medias = []
alunos_acima_7 = 0

for i in range(1, 6):
    print(f"Notas do aluno {i}:")
    soma_notas = 0
    for j in range(1, 5):
        nota = float(input(f" Digite a nota {j}: "))
        soma_notas += nota
    
    media = soma_notas / 4
    medias.append(media)
    if media >= 7.0:
        alunos_acima_7 += 1

print(f"\nNúmero de alunos com média >= 7.0: {alunos_acima_7}")