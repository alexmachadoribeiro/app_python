# TODO atividade:
"""
Crie um programa em que o usuário informa várias notas de um aluno de 0 a 10 (quantas notas ele quiser inserir), e ao final, o programa calcule a média desse aluno e informa se ele está aprovado, de recuperação ou reprovado.
"""
# NOTE: média para aprovação: 7. Média para recuperação: entre 5 e 7. Abaixo de 5: reprovado.
# NOTE: usar replace() para substituir a vírgula por ponto em valores decimais. Exemplo:
nota = float(input("Informe um número decimal: ").replace(",", "."))
print(f"{nota} - {type(nota)}")
