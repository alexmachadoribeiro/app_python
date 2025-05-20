def fazer_deposito(saldo, valor):
    saldo += valor
    return saldo

def fazer_saque(saldo, valor):
    saldo -= valor
    return saldo

def consultar_dados(titular):
    print(f"{'-'*20} Dados da conta {'-'*20}\n")
    print(f"Titular: {titular.get('nome')}")
    print(f"CPF do titular: {titular.get('cpf')}")
    print(f"Agência do titular: {titular.get('agencia')}")
    print(f"Número da conta do titular: {titular.get('num_conta')}")
    print(f"Saldo da conta do titular: R$ {titular.get('saldo')}")