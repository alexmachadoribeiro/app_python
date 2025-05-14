# importa módulo
from funcoes import calcular_quadrilatero, calcular_triangulo

if __name__ == "__main__":
    try:
        print("Escolha a figura da qual deseja calcular a área:\n")
        print("1 - Quadrilátero")
        print("2 - Triângulo")
        opcao = input("Opção desejada: ")
        if opcao == "1" or opcao == "2":
            b = float(input("Informe o valor da base: ").replace(",", "."))
            h = float(input("Informe o valor da altura: ").replace(",", "."))
            match opcao:
                case "1":
                    resultado = calcular_quadrilatero(b, h)
                    print(f"Área do quadrilátero: {resultado}")
                case "2":
                    resultado = calcular_triangulo(b, h)
                    print(f"Área do triângulo: {resultado}")
        else:
            print("Opção inválida. Programa encerrado!")
    except Exception as e:
        print(f"Não foi possível executar a operação. {e}.")