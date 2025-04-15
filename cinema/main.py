# tratamento de exceção
try:
    # declaração de variáveis
    nome = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))

    # laço de repetição
    while True:
        # exibe o menu
        print(f"{'-'*20}LISTA DE FILMES{'-'*20}\n")
        print("Sala 1 - A Roda Quadrada - Livre")
        print("Sala 2 - A Volta dos Que Não Foram - 12 anos")
        print("Sala 3 - As Tranças do Rei Careca - 14 anos")
        print("Sala 4 - Poeira em Alto Mar - 16 anos")
        print("Sala 5 - A Vingança do Peixe Frito - 18 anos")

        # recebe a sala desejada pelo usuário
        sala = input("\nInforme o número da sala: ")

        # verifica a sala escolhida
        match sala:
            case "1":
                idade_minima = 0
            case "2":
                idade_minima = 12
            case "3":
                idade_minima = 14
            case "4":
                idade_minima = 16
            case "5":
                idade_minima = 18
            case _:
                idade_minima = idade+1
        
        # verifica se o usuário tem a idade mínima
        if idade >= idade_minima:
            print(f"Sala {sala} escolhida. Tenha um bom filme.")
            break
        else:
            print(f"{nome} não possui idade para ver o filme.")
            print("Favor selecionar outra sala.")
            continue
except Exception as e:
    print(f"Não foi possível executar a operação. {e}.")
finally:
    print("Programa encerrado.")
'''
Crie um algoritmo que receba o nome do usuário e sua idade e informe o nome de 5 filmes, e suas respectivas salas (sala 1 a sala 5), e também suas respectivas classificações indicativas. O usuário deverá escolher o filme e o programa irá verificar se o usuário tem a idade mínima para ver o filme. Caso tenha, o programa imprime o bilhete e encerra. Caso não tenha a idade mínima, o programa retornará para a tela de seleção de filmes, permitindo que o usuário escolha outro filme.
'''