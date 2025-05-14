# declaração de função
def dar_boas_vindas(nome, curso):
    return f"{nome}, seja bem vindo ao curso de {curso}!"

# algoritmo principal
nome = input("Informe seu nome: ")
curso = input("Informe o nome do seu curso: ")
saida = dar_boas_vindas(nome, curso)

print(saida)