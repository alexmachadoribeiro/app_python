# importando a biblioteca
import os

# declaração da lista
lista = []

# tratamento de exceção
try:
    # loop infinito
    while True:
        item = input("Informe o nome do item ou deixe em branco para encerrar: ") #input
        os.system("cls") # limpa o terminal

        # verifica se o item está vazio ou não
        if item != "":
            lista.append(item) # insere o item na lista
            print(f"{item} inserido na lista com sucesso!") # mensagem de confirmação
            continue
        else:
            break
    
    # ordena a lista
    lista.sort()
except Exception as e:
    print(f"Não foi possível inserir item na lista. {e}.")
finally:
    print("Lista de itens:\n")
    for item in lista:
        print(item)

'''
Crie um programa que receba do usuário uma lista de compras e ordene a lista em ordem alfabética.
Obs 1: só quero os nomes dos itens, deixe os preços e a quantidade de fora.
Obs 2: após terminarem, façam o commit no GitHub.
'''