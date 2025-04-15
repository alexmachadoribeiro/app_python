# declaração de variáveis
x = float(input("Informe o valor de x: "))
y = float(input("Informe o valor de y: "))

# mostra o menu
print("Escolha a operação desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Resto da Divisão")

# usuário escolhe a operação
operador = input("Informe a operação desejada: ")

# estrutura match
match operador:
    case "1":
        print(f"Resultado da soma: {x+y}.")
    case "2":
        print(f"Resutlado da subtração: {x-y}.")
    case "3":
        print(f"Resultado da multiplicação: {x*y}.")
    case "4":
        print(f"Resultado da divisão: {x/y}.")
    case "5":
        print(f"Resto da divisão: {x%y}.")
    case _:
        print("Operador inválido.")