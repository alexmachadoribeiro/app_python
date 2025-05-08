# dicionário vazio
usuario = {}

try:
    # entrada de dados
    usuario["nome"] = input("Informe o nome: ")
    usuario["data de nascimento"] = input("Informe a data de nascimento: ")
    usuario["cpf"] = input("Informe o CPF: ")
    usuario["email"] = input("Informe o e-mail: ")
    usuario["gênero"] = input("Informe o gênero: ")
    usuario["telefone"] = input("Informe o telefone: ")
    usuario["altura"] = float(input("Informe a altura em metros: ").replace(",", "."))
    usuario["peso"] = float(input("Informe o peso em kg: ").replace(",", "."))
    usuario["tipo sanguíneo"] = input("Informe o tipo sanguíneo: ")

    # exibe os dados do usuário
    for chave in usuario:
        print(f"{chave.title()}: {usuario.get(chave)}")
    
    # calcula o imc do usuário
    imc = usuario.get("peso")/usuario.get("altura")**2

    # exibe o valor do imc
    print(f"IMC de {usuario.get("nome")}: {imc:,.2f}")

    # exibe o diagnóstico do usuário com base no valor do imc
    if imc <= 18.5:
        print(f"{usuario.get("nome")} está abaixo do peso.")
    elif imc < 25:
        print(f"{usuario.get("nome")} está no peso ideal. PARABÉNS!!!")
    elif imc < 30:
        print(f"{usuario.get("nome")} está acima do peso ideal.")
    elif imc < 35:
        print(f"{usuario.get("nome")} está obeso.")
    elif imc < 40:
        print(f"{usuario.get("nome")} está com obesidade nível II.")
    else:
        print(f"{usuario.get("nome")} está com obesidade mórbida. PROCURE UM MÉDICO!!!")
except Exception as e:
    print(f"Não foi possível inserir os dados. {e}.")
"""
Crie um programa que inicializa um dicionário zerado, e o usuário adiciona e insere os seguintes dados:
Nome, Data de Nascimento, CPF, E-mail, Gênero, Telefone, Altura, Peso, Tipo Sanguíneo;
Ao final, o programa exibe os dados do usuário e informa seu IMC.
"""
# NOTE: o usuário deverá informar o valor apenas dessas chaves.
# NOTE: o programa deverá exibir os dados em linhas diferentes.
# NOTE: o resultado do IMC deverá ser arredondado para 2 casas decimais.
# NOTE: mostre o diagnóstico do usuário de acordo com o valor do IMC.