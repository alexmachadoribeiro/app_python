# declaração de variáveis
nome = input("Informe o nome do aluno: ")
nota = float(input("Informe a nota do aluno: "))

# verifica se o aluno passou ou não
if nota >= 0 and nota <= 10:
    if nota >= 7:
        print(f"{nome} está aprovado.")
    elif nota >= 5:
        print(f"{nome} está de recuperação.")
    else:
        print(f"{nome} está reprovado.")
else:
    print("Nota inválida.")