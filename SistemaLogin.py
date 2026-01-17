# Sistema de Login
usuario = input("Login: ")
senha = input("Senha: ")

if usuario == "admin" and senha == "admin123":
    print("Acesso permitido. Bem-vindo!")
else:
    print("Erro: Usuário ou senha incorretos.")