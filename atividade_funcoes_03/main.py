import os
import random as r
import modulo as m

if __name__ == "__main__":
    titular = {}
    try:
        while True:
            # ANCHOR - menu
            print(f"{'='*30} BNACO COBRA {'='*30}\n")
            print("0 - Sair do programa.")
            print("1 - Criar nova conta.")
            print("2 - Alterar dados do titular da conta.")
            print("3 - Fazer saque.")
            print("4 - Fazer depósito.")
            print("5 - Constular dados da conta.")
            opcao = input("Informe a opção desejada: ")
            os.system("cls")
            match opcao:
                case "0":
                    print("Programa encerrado com sucesso.")
                    print("Tenha um ótimo dia.")
                    break
                case "1":
                    titular['agencia'] = 1010
                    titular['num_conta'] = r.randint(10000, 99999)
                    titular['saldo'] = 0.00
                    titular['nome'] = input("Informe o nome do titular: ")
                    titular['cpf'] = input("Informe o CPF do titular: ")

                    os.system("cls")
                    print(f"Conta {titular.get('num_conta')} criada com sucesso.\n")

                    continue
                case "2":
                    print(f"Nome: {titular.get('nome')}")
                    print(f"CPF: {titular.get('cpf')}\n")
                    campo = input("Informe o campo que deseja alterar: ").strip().lower()
                    match campo:
                        case "nome":
                            titular['nome'] = input("Informe o novo nome do titular: ")

                            os.system("cls")
                            print("Nome do titular atualizado com sucesso.")
                        case "cpf":
                            titular['cpf'] = input("Informe o novo CPF do titular: ")

                            os.system("cls")
                            print("CPF do titular atualizado com sucesso")
                        case _:
                            print("Campo inválido")

                    continue
                case "3":
                    valor = float(input("Informe o valor do saque: R$ ").replace(",", "."))
                    saldo = titular.get('saldo')

                    if valor <= saldo:
                        titular['saldo'] = m.fazer_saque(saldo, valor)

                        os.system("cls")
                        print("Saque efetuado com sucesso.")
                        print(f"Saldo: R$ {titular.get('saldo'):,.2f}\n")
                    else:
                        print("Não foi possível efetuar o saque. Valor indisponível.")
                    
                    continue
                case "4":
                    valor = float(input("Informe o valor do depósito: R$ ").replace(",", "."))
                    titular['saldo'] = m.fazer_deposito(titular.get('saldo'), valor)

                    os.system("cls")
                    print("Depósito efetuado com sucesso.")
                    print(f"Saldo: R$ {titular.get('saldo'):,.2f}\n")

                    continue
                case "5":
                    m.consultar_dados(titular)
                    continue
                case _:
                    print("Opção inválida.")
                    continue
    except Exception as e:
        print(f"Não foi possível executar a operação. {e}.")

# TODO - atividade
"""
Crie um programa onde o usuário escolhe uma dessas opções do menu:
0 - Sair do programa.
1 - Criar nova conta
2 - Alterar dados do titular da conta
3 - Fazer saque
4 - Fazer depósito
5 - Consultar dados da conta
Dados do titular da conta:
- Nome
- CPF
- Agência (1010)
- Número da conta (número aleatório)
- Saldo (sempre vai começar em zero)
"""
# NOTE - Consultar dados da conta envolve consultar saldo da conta
# NOTE - Para número da conta, use a biblioteca random
