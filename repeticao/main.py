# tratamento de exceção
try:
    # repetição do algoritmo
    while True:
        # declaração de variáveis
        nome = input("Informe o seu nome: ")
        idade = int(input("Informe sua idade: "))

        # saída de dados
        print(nome, "é maior de idade." if idade >= 18 else "é menor de idade.")

        # decisão
        continuar = input("Deseja continuar? (s/n)")

        match continuar:
            case "s":
                continue
            case "n":
                break
            case _:
                print("Não foi possível computar sua decisão.")
                continue
except Exception as e:
    print(f"Dados informados inválidos. {e}.")
finally:
    print("Programa finalizado com sucesso.")