# Carrinho de Compras (Dicionário)

carrinho = {
    "Arroz": 2,
    "Feijão": 3,
    "Macarrão": 5
}

# Simulando preços fixos para o cálculo
precos = {"Arroz": 25.0, "Feijão": 9.0, "Macarrão": 4.5}
total = 0

for produto, quantidade in carrinho.items():
    valor_item = quantidade * precos[produto]
    total += valor_item
    print(f"{produto}: {quantidade} un x R${precos[produto]} = R${valor_item}")

print(f"Total do carrinho: R$ {total:.2f}")