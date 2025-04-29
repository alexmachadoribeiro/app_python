# NOTE: o JOIN é um comando que pega os valores de uma lista e junta em uma única variável.

# lista de dias da semana
dias = [
    "Domingo", 
    "Segunda-Feira", 
    "Terça-Feira", 
    "Qaurta-Feira", 
    "Quinta-Feira",
    "Sexta-Feira",
    "Sábado"
]

separador = ", " # delimitador
semana = separador.join(dias) # junta os itens da lista

# exibe na tela
print(semana)
