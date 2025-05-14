# declaração de função
def calcular_triangulo(b, h):
    area = (b*h)/2
    return area

# algoritmo principal
try:
    b = float(input("Informe o valor da base: ").replace(",", "."))
    h = float(input("Informe o valor da altura: ").replace(",", "."))
    area = calcular_triangulo(b, h)

    print(f"O valor da área do triângulo é {area}.")
except Exception as e:
    print(f"Não foi possível calcular a área do triângulo. {e}.")