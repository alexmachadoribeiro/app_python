# importa biblioteca
import os

# declaração da lista
cidades = [
    "Brasília", "Rio De Janeiro", "São Paulo", 
    "Belo Horizonte", "Goiânia", "Palmas", 
    "Brasília", "Goiânia", "Brasília"
]

# tratamento de exceção
try:
    # loop infinito
    while True:
        os.system("cls") # limpa o terminal
        pesquisa = input("Informe a cidade a ser pesquisada: ").title()
        result = cidades.count(pesquisa) # retorna quantidade de valores encontrados

        # mostra resultado na tela
        if result != 0:
            print(f"{pesquisa} foi encontrado na lista {result} vezes.")
        else:
            print(f"{pesquisa} não foi encontrado na lista.")
        
        # pergunta se o usuário deseja realizar uma nova pesquisa
        continuar = input("Deseja continuar? (s/n): ")

        # verifica se o usuário deseja continuar
        match continuar:
            case "s":
                continue
            case "n":
                break
            case _:
                print("Opção inválida.")
                break
except Exception as e:
    print(f"Não foi possível realizar a busca. {e}.")