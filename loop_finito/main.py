# tratamento de exceção
try:
    # declaração de variável
    n = int(input("Informe um número inteiro positivo: "))

    # loop
    while n >= 0:
        print(n)
        n -= 1
except Exception as e:
    print(f"Número inválido. {e}.")