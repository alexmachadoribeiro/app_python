# declaração de variáveis
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

# operador ternário
result = "é maior de idade" if idade >= 18 else "é menor de idade"

# exibe o resultado na tela
print(f"{nome} {result}.")