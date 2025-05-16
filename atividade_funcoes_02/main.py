# declaração de função
def calcular_fibonacci(n):
    return n if n <= 1 else calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

# algoritmo principal
if __name__ == "__main__":
    try:
        n = int(input("Informe o número da sequência de Fibonacci desejado: "))

        for i in range(1, n+1):
            print(calcular_fibonacci(i))
    except Exception as e:
        print(f"Não foi possível calcular a sequência de Fibonacci. {e}.")