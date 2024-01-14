# Variáveis de inicialização
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Menu de operações
menu = """
Qual operação deseja realizar?

----Menu----
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
------------

"""

# Loop principal
while True:
    # Recebe a opção do usuário
    opcao = int(input(menu))

    # Opção 1: Depositar
    if opcao == 1:
        print("Opção de depósito selecionada")
        valor = float(input("Qual valor será depositado?"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} \n"
        else:
            print("Operação falhou, digite um valor válido.")

    # Opção 2: Sacar
    elif opcao == 2:
        print("Opção de Saque selecionada")
        valor = float(input("Quanto deseja sacar?"))
            
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou, saldo insuficiente!")
        elif excedeu_limite:
            print("Operação falhou, o valor excedeu o limite permitido para saque.")
        elif excedeu_saques:
            print("Operação falhou, você excedeu o limite de saques permitidos.")
        elif valor > 0:
            print("Saque realizado com sucesso, retire o dinheiro na boca do caixa.")
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
        else:
            print("Operação falhou, digite um valor válido.")

    # Opção 3: Extrato
    elif opcao == 3:
        print("==================== Extrato ====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================================")

    # Opção 4: Sair do programa
    elif opcao == 4: 
        break

    # Opção inválida
    else:
        print("Opção inválida, verifique se escolheu corretamente.")
