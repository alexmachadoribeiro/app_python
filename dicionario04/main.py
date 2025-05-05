import os

dados = {
    'nome': "Alex Machado",
    'idade': 40,
    'cpf': "666.666.666-66"
}

try:
    while True:
        os.system("cls")
        for chave in dados:
            print(f"{chave.title()}: {dados.get(chave)}.")

        # usuário informa se deseja inserir nova chave ou encerra
        prosseguir = input("Deseja inserir novos dados? (s/n): ")
        
        match prosseguir:
            case "s":
                # usuário informa os dados
                nova_chave = input("\nInforme o nome da nova chave: ")
                dados[nova_chave] = input(f"Informe o valor de {nova_chave}: ")
                continue
            case "n":
                break
            case _:
                print("Opção inválida.")
                continue
except Exception as e:
    print(f"Não foi possível inserir a nova chave. {e}.")