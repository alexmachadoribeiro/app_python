import os
import math

def calcular_1o_grau(a, b):
    x = -b/a
    return x

def calcular_2o_grau(a, b, c):
    if a is not 0:
        delta = (b**2) - 4*a*c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            yield f"x' = {x1}"
            yield f'x" = {x2}'
        elif delta == 0:
            x = -b / 2*a
            yield f"x = {x}"
        else:
            yield "A equação não possui valores reais."
    else:
        yield "O valor de 'a' é zero, e portanto não é uma equação do 2º grau."

if __name__ == "__main__":
    try:
        while True:
            print("1 - Calcular equação do 1º grau.")
            print("2 - Calcular equação do 2º grau.")
            print("3 - Sair do programa.")
            opcao = input("Informe a opção desejada: ")
            match opcao:
                case "1":
                    os.system("cls")

                    a = float(input("Informe o valor de 'a': ").replace(",", "."))
                    b = float(input("Informe o valor de 'b': ").replace(",", "."))
                    result = calcular_1o_grau(a, b)

                    print(f"O valor de x em {a}x + {b} = 0 é: {result}.")
                    continue
                case "2":
                    os.system("cls")

                    a = float(input("Informe o valor de 'a': ").replace(",", "."))
                    b = float(input("Informe o valor de 'b': ").replace(",", "."))
                    c = float(input("Informe o valor de 'c': ").replace(",", "."))
                    result = calcular_2o_grau(a, b, c)

                    for x in result:
                        print(x)
                    
                    continue
                case "3":
                    print("Programa encerrado com sucesso.")
                    break
                case _:
                    print("Opção inválida.")
                    continue
    except Exception as e:
        print(f"Não foi possível fazer o cálculo. {e}.")

# TODO - atividade
"""
Crie um programa onde o usuário poderá escolher se deseja calcular a equação do 1º grau ou  a equação do 2º grau, e o programa retorna o resultado da equação.
"""
# NOTE - o programa deverá ser executado em loop.
# NOTE - esta atividade deverá ser feita com funções.