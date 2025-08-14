#Sistema Bancario Simples

# Variáveis 
saldo = 0.0
historico = []
saques_hoje = 0
LIMITE_SAQUES = 3
MAX_SAQUE = 500.00

def mostrar_menu():
    """Exibe o menu de opções"""
    print("\n" + "="*30)
    print("BANCO PYTHON".center(30))
    print("="*30)
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver Extrato")
    print("4 - Sair")
    print("="*30)

def processar_deposito():
    """Adiciona dinheiro na conta"""
    global saldo, historico
    
    try:
        valor = float(input("Valor para depositar: R$ "))
        if valor > 0:
            saldo += valor
            historico.append(f"Depósito: +R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado!")
        else:
            print("O valor precisa ser positivo!")
    except:
        print("Valor inválido! Use números.")

def processar_saque():
    """Retira dinheiro da conta"""
    global saldo, historico, saques_hoje
    
    #  limites
    if saques_hoje >= LIMITE_SAQUES:
        print(f"Você já fez {LIMITE_SAQUES} saques hoje.")
        return
        
    try:
        valor = float(input("Valor para sacar: R$ "))
        
        if valor <= 0:
            print("Valor deve ser positivo!")
        elif valor > MAX_SAQUE:
            print(f"Limite por saque: R$ {MAX_SAQUE:.2f}")
        elif valor > saldo:
            print("Saldo insuficiente!")
        else:
            saldo -= valor
            historico.append(f"Saque: -R$ {valor:.2f}")
            saques_hoje += 1
            print(f"Saque de R$ {valor:.2f} realizado!")
    except:
        print("Valor inválido! Use números.")

def mostrar_extrato():
    """Exibe todas as movimentações"""
    print("\n" + "="*15 + " EXTRATO " + "="*15)
    
    if not historico:
        print("Nenhuma movimentação ainda.")
    else:
        for movimento in historico:
            print(movimento)
    
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("="*38)

# logica principal
if _name_ == "_main_":
    while True:
        mostrar_menu()
        opcao = input("Escolha: ")
        
        if opcao == "1":
            processar_deposito()
        elif opcao == "2":
            processar_saque()
        elif opcao == "3":
            mostrar_extrato()
        elif opcao == "4":
            print("Obrigado por usar o Banco Python!")
            break
        else:
            print("Opção inválida! Tente novamente.")
