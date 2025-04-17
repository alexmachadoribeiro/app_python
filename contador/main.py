# tratamento de exceção
try:
    # declaração de variável
    n = int(input("Informe um número inteiro positivo: "))

    # laço for
    for n in range(n, -1, -1):
        print(n)
except Exception as e:
    print(f"Não foi possível realizar a contagem. {e}.")