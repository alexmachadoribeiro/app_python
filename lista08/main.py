# importa biblioteca
import os

# declaração da lista
cidades = ["Brasília", "São Paulo", "Rio De janeiro", "Curitiba", "Recife", "Fortaleza"]

# tratamento de exceção
try:
    # loop infinito
    while True:
        # exibe a lista
        for i in range(len(cidades)):
            print(f"Cidade de código {i}: {cidades[i]}.")
        # usuário informa se deseja alterar algum valor
        alterar = input("\nDeseja alterar algum valor? (s/n)")
        match alterar:
            case "s":
                codigo_cidade = int(input("\nInforme o código da cidade que deseja mudar: "))
                nova_cidade = input("Informe o novo nome da cidade: ")
                cidades[codigo_cidade] = nova_cidade
                os.system("cls")
                continue
            case "n":
                break
            case _:
                print("Opção inválida")
                break
except Exception as e:
    print(f"Não foi possível alterar valor na lista. {e}.")