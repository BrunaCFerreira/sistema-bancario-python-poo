class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
    
class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    def sacar(self, valor):
        if valor > self.saldo:
            return False
        elif valor > 0:
            self.saldo -= valor
            return True
        else:
            return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True 
        else:
            return False

class ContaCorrente(Conta):
    def __init__(self, limite, limite_saques, numero, cliente):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Transacao:
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        sucesso_na_transacao = conta.depositar(self.valor)

        if sucesso_na_transacao:
            conta.historico.adicionar_transacao(self)
            print("\n === Depósito realizado com sucesso! ===")
        else:
            print("\n === A operação falhou, o valor informado é inválido! ===")

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        sucesso_na_transacao = conta.sacar(self.valor)

        if sucesso_na_transacao:
            conta.historico.adicionar_transacao(self)
            print("\n === Saque realizado com sucesso! ===")

        else:
            print("\n === A operação falhou ! Saldo insuficiente ou valor inválido. ===")

def menu():
    print("=============MENU=============")
    print("[d] - Depositar")
    print("[s] - Sacar")
    print("[e] - Extrato")
    print("[nu] - Novo Usuário")
    print("[nc] - Nova Conta")
    print("[q] - Sair")

    return input ("Digite a letra referente a operação que deseja realizar: ")

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            print("\n --- Depósito ---")
            cpf = input ("Informe o CPF do cliente (somente números): ")

            cliente_encontrado = None
            for cliente in clientes:
                if cliente.cpf == cpf:
                    cliente_encontrado = cliente
                    break
            
            if not cliente_encontrado:
                print(" === Cliente não encontrado! ===")
                continue

            if not cliente_encontrado.contas:
                print(" === O cliente não possui nenhuma conta ===")

            valor_digitado = float(input("Informe o valor do depósito: R$ "))

            transacao = Deposito(valor_digitado)
            conta = cliente_encontrado.contas[0]
            cliente_encontrado.realizar_transacao(conta, transacao)
            


        elif opcao == "s":
            print("\n --- Saque ---")
            cpf = input ("Informe o CPF do cliente (somente números): ")

            cliente_encontrado = None
            for cliente in clientes:
                if cliente.cpf == cpf:
                    cliente_encontrado = cliente
                    break
            
            if not cliente_encontrado:
                print(" === Cliente não encontrado! ===")
                continue

            if not cliente_encontrado.contas:
                print(" === O cliente não possui nenhuma conta ===")

            valor_digitado = float(input("Informe o valor do saque: R$ "))

            transacao = Saque(valor_digitado)
            conta = cliente_encontrado.contas[0]
            cliente_encontrado.realizar_transacao(conta, transacao)
            

        elif opcao == "e":
            print("\n --- Extrato ---")
            cpf = input("Informe o CPF do cliente (somente números): ")

            cliente_encontrado = None
            for cliente in clientes:
                if cliente.cpf == cpf:
                    cliente_encontrado = cliente
                    break
             
            if not cliente_encontrado:
                print("=== Cliente não encontrado ===")
                continue

            if not cliente_encontrado.contas:
                print(" === O cliente não possui nenhuma conta ===")
                continue

            conta = cliente_encontrado.contas[0]
            print("\n========== Extrato ==========")

            if not conta.historico.transacoes:
                print("Não foram realizadas movimentações.")
            else:
                for transacao in conta.historico.transacoes:
                    tipo = transacao.__class__.__name__
                    print(f"{tipo}:\t\t R$ {transacao.valor:.2f}")

            print(f"\nSaldo Atual:\t R$ {conta.saldo:.2f}")
            print("==================================================")

        elif opcao == "nu":
            print("\n --- Cadastro de Novo Usuário ---")
            cpf = input("Informe o CPF (somente números): ")
            nome = input("Informe o nome completo: ")
            data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            endereco = input("Informe o endereço (Logradouro, nro - bairro - cidade/sigla estado): ")

            novo_cliente = PessoaFisica(endereco, cpf, nome, data_nascimento)
            clientes.append(novo_cliente)

            print("Usuário criado com sucesso!")

        elif opcao == "nc":
            print("\n --- Cadastro de Nova Conta ---")
            cpf = input("Informe o CPF do cliente (somente números): ")

            cliente_encontrado = None
            for cliente in clientes:
                if cliente.cpf == cpf:
                    cliente_encontrado = cliente
                    break
            
            if cliente_encontrado:
                numero_conta = len(contas) + 1

                nova_conta = ContaCorrente(limite=500.0, limite_saques=3, numero=numero_conta, cliente=cliente_encontrado)

                cliente_encontrado.adicionar_conta(nova_conta)
                contas.append(nova_conta)

                print(f"=== Conta criada com sucesso! Agência 0001  Número: {numero_conta} ===")

            else:
                print(" === Cliente não encontrado! Por favor, faça o cadastro do usuário primeiro ===")

        elif opcao == "q":
            print("Saindo do sistema.... Até logo")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")

main()