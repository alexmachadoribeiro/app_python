import os

lista = []

try:
    while True:
        usuario = {}

        print(f"{'='*20} CRUD COBRA {'='*20}")
        print("O que deseja fazer?")
        print("0 - Sair do programa")
        print("1 - Cadastrar novo usuário")
        print("2 - Listar todos os usuários")
        print("3 - Alterar os dados de um usuário")
        print("4 - Excluir um usuário")

        opcao = input("\nInforme a opção desejada: ")

        match opcao:
            case "0":
                print("\nPrograma encerrado!\n")
                break
            case "1":
                usuario['nome'] = input("Informe o nome do usuário: ")
                usuario['cpf'] = input("Informe o CPF do usuário: ")
                usuario['email'] = input("Informe o e-mail do usuário: ")
                usuario['telefone'] = input("Informe o telefone do usuário: ")
                usuario['data de nascimento'] = input("Informe a data de nascimento do usuário: ")
                usuario['genero'] = input("Informe o gênero do usuário: ")

                lista.append(usuario)
                os.system("cls")
                print(f"{usuario.get('nome')} cadastrado com sucesso!\n")
                continue
            case "2":
                os.system("cls")
                for i in range(len(lista)):
                    print(f"Posição: {i}")
                    for chave in lista[i]:
                        print(f"{chave.title()}: {lista[i].get(chave)}")
                    print("\n")
                continue
            case "3":
                os.system("cls")
                posicao = int(input("Informe a posição do usuário que deseja alterar: "))
                if lista[posicao]:
                    for chave in lista[posicao]:
                        print(f"{chave.title()}: {lista[posicao].get(chave)}")
                    print("\n")
                    dado = input("Informe o nome da chave que deseja alterar: ")
                    if lista[posicao][dado]:
                        lista[posicao][dado] = input(f"Informe o novo valor de {dado}: ")
                        os.system("cls")
                        print("Dados alterados com sucesso!\n")
                    else:
                        print("Chave inválida!")
                else:
                    print("Posição inválida!")
                continue
            case "4":
                os.system("cls")
                posicao = int(input("Informe a posição do usuário que deseja deletar: "))
                if lista[posicao]:
                    del(lista[posicao])
                    os.system("cls")
                    print("Usuário deletado com sucesso!")
                else:
                    print("Não foi possível deletar o usuário!")
                continue
            case _:
                print("Opção inválida!")
                continue
except Exception as e:
    print(f"Não foi possível executar a operação. {e}.")

"""
Crie um CRUD, ou seja, um programa que:
- Cadastre
- Liste
- Altere
- Exclua

O programa deverá cadastrar pessoas com os seguintes dados:
Nome, CPF, E-mail, Telefone, Data de Nascimento, Gênero
"""
# NOTE: o usuário poderá cadastrar quantas pessoas quiser.
# NOTE: o programa deverá fornecer um menu com as opções: cadastrar, listar, alterar, excluir e sair do programa.