# importa bibilotecas
import time
import os

# tratamento de exceção
try:
    # declaração de variável
    n = int(input("Informe um número inteiro positivo: "))

    # laço de repetição
    for n in range(n, -1, -1):
        os.system("cls")
        print(f"{n}...")
        time.sleep(1)
    # mensagem final
    print("BOOOMMMM!!!!")
    print("A cobra explodiu!!!")
except Exception as e:
    print(f"Não foi possível realizar a contagem regressiva. {e}.")