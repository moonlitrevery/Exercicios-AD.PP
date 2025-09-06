class Item:
    def __init__(self, nome: str, preco: float, qtd: int = 1):
        if preco <= 0:
            raise ValueError("O preço deve ser positivo.")
        if qtd <= 0:
            raise ValueError("A quantidade deve ser positiva.")
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def subtotal(self) -> float:
        return self.preco * self.qtd


class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item: Item):
        self.itens.append(item)

    def remover_item(self, nome: str):
        for item in self.itens:
            if item.nome == nome:
                self.itens.remove(item)
                return
        raise ValueError(f"Item '{nome}' não encontrado no carrinho.")

    def calcular_total(self) -> float:
        return sum(item.subtotal() for item in self.itens)

    def listar_itens(self) -> list:
        return [(item.nome, item.qtd, item.preco, item.subtotal()) for item in self.itens]


if __name__ == "__main__":
    carrinho = Carrinho()

    while True:
        print("\n--- Menu Carrinho ---")
        print("1 - Adicionar item")
        print("2 - Remover item")
        print("3 - Listar itens")
        print("4 - Mostrar valor total")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                nome = input("Nome do item: ")
                preco = float(input("Preço do item: "))
                qtd = int(input("Quantidade: "))
                carrinho.adicionar_item(Item(nome, preco, qtd))
                print(f"{qtd}x {nome} adicionado(s) ao carrinho.")

            elif opcao == "2":
                nome = input("Nome do item a remover: ")
                carrinho.remover_item(nome)
                print(f"Item '{nome}' removido do carrinho.")

            elif opcao == "3":
                print("\nItens no carrinho:")
                for nome, qtd, preco, subtotal in carrinho.listar_itens():
                    print(f"{nome} - {qtd}x R${preco:.2f} = R${subtotal:.2f}")

            elif opcao == "4":
                print(f"\nValor do carrinho: R${carrinho.calcular_total():.2f}")

            elif opcao == "0":
                print("Saindo...")
                break

            else:
                print("Opção inválida!")

        except ValueError as e:
            print(f"Erro: {e}")
