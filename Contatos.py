# Dicionário de Contatos

contatos = {
    "Ana": "11 9999-8888",
    "Bruno": "21 7777-6666",
    "Carla": "31 5555-4444"
}

busca = input("Digite o nome para procurar o telefone: ")
print(contatos.get(busca, "Contato não encontrado."))