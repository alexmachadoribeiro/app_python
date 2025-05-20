calcular_pg = lambda x: x * 2 # lambda
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9] # lista numérica
result = list(map(calcular_pg, numeros))

print("Progressão geométrica:\n")
for n in result:
    print(n)