import os

nomes = ["Fulano", "Cicrano", "Beltrano", "João", "Maria", "José"]

try:
    for i in range(len(nomes)):
        print(f"Código {i}: {nomes[i]}.")
    posicao = int(input("Informe o código do item a ser separado: "))
    nome_separado = nomes.pop(posicao) # separa o item da lista
    os.system("cls")
    print(nome_separado)
except Exception as e:
    print(f"Não foi possível separar o item da lista. {e}.")