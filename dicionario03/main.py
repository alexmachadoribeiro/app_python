# biblioteca
import os

# dicionário
dados = {
    'nome': "Alex Machado",
    'idade': 40,
    'cpf': "666.666.666-66"
}

# exibe os dados do dicionário
for chave in dados:
    print(f"{chave.title()}: {dados.get(chave)}.")

# usuário insere nova chave (email)
dados['email'] = input("\nInforme o e-mail do usuário: ")

# limpa terminal e re-exibe a lista
os.system('cls')
for chave in dados:
    print(f"{chave.title()}: {dados.get(chave)}.")