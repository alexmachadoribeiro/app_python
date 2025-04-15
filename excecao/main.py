# tratamento de exceção
try:
    # declaração de variável
    x = int(input("Informe um número inteiro: "))

    # saída de dados
    print(f"O número informado foi {x}.")
except Exception as e:
    print(f"Não foi possível ler o número informado pelo usuário. {e}")
finally:
    print("Meu programa foi executado com sucesso!")