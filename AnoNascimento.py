#2. Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.

ano_nascimento = int(input("Informe o seu ano de nascimento: "))
ano_atual = 2026 # Definido conforme o ano atual do sistema

idade = ano_atual - ano_nascimento

print(f"Você tem (ou fará) {idade} anos em {ano_atual}.")