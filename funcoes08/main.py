import math

# função normal
# def calcular_area_circulo(r):
#     area = math.pi * r**2
#     return area

# função lambda
calcular_area_circulo = lambda r: math.pi * r**2

if __name__ == "__main__":
    try:
        r = float(input("Informe o raio do círculo: "))
        result = calcular_area_circulo(r)

        print(f"A área do círculo é {result:,.2f}.")
    except Exception as e:
        print(f"Não foi possível calcular a área do círculo. {e}.")