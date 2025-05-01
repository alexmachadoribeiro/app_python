# dicionário
usuario = dict(nome="Fulano de Tal", idade=18, email="fulano@gmail.com")

# exibindo os dados do dicionário
for chave in usuario:
    print(f"{chave.title()}: {usuario.get(chave)}.")