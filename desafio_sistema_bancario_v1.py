
# Desafio: Sistema Bancário
# Versão 1.0
# Descrição: Este script implementa um sistema bancário simples que permite depósitos, saques e exibição de extrato.



print ("\n - Bem vindo(a) ao Sistema Bancário! - \n")



conta_cliente = input("+ Informe o número da sua conta -> ")

contas_cadastradas = ["123456789", "987654321", "112233445"]

if conta_cliente not in contas_cadastradas:
    print("\nConta não encontrada. Tente novamente!")
    exit()

else:
    print(f"Conta {conta_cliente} encontrada com sucesso!")


menu = """

Bem vindo(a) ao Sistema Bancário!
- Selecione a operação desejada: -

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d" or opcao == "D":
        valor = float(input("Informe o valor do depósito: "))

        # Verifica se o valor é positivo
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s" or opcao == "S":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        # Verifica se o valor do saque é positivo e se não excede os limites
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            
        # Se o valor for válido, atualiza o saldo e o extrato
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    # Exibe o extrato e o saldo
    elif opcao == "e" or opcao == "E":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q" or opcao == "Q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")