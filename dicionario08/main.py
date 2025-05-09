# lista de dicionários
pessoas = [
    {
        'nome': "Fulano de Tal",
        'idade': 18,
        'email': "fulano@gmail.com"
    },
    {
        'nome': "Cirano de Souza",
        'idade': 25,
        'email': "cicrano@gmail.com"
    },
    {
        'nome': "Beltrano da Silva",
        'idade': 30,
        'email': "beltrano@gmail.com"
    }
]

for pessoa in pessoas:
    print(f"\n{'-'*20}\n")
    for chave in pessoa:
        print(f"{chave.title()}: {pessoa.get(chave)}.")