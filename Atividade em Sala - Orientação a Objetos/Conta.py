class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para saque.")
        self.saldo -= valor

    def extrato(self) -> str:
        return f"Conta: {self.numero} | Titular: {self.titular} | Saldo: {self.saldo:.2f}"


if __name__ == "__main__":
    numero = input("Digite o número da conta: ")
    titular = input("Digite o nome do titular: ")
    conta = Conta(numero, titular)

    while True:
        print("\n--- Menu ---")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                valor = float(input("Valor do depósito: "))
                conta.depositar(valor)
                print("Depósito realizado com sucesso!")
            elif opcao == "2":
                valor = float(input("Valor do saque: "))
                conta.sacar(valor)
                print("Saque realizado com sucesso!")
            elif opcao == "3":
                print(conta.extrato())
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")
        except ValueError as e:
            print(f"Erro: {e}")
