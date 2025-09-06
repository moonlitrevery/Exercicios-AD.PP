ANO_ATUAL = 2025

class Midia:
    def __init__(self, titulo: str, ano: int):
        self.titulo = titulo
        self.ano = ano

    @property
    def idade(self) -> int:
        return ANO_ATUAL - self.ano


class Filme(Midia):
    def __init__(self, titulo: str, ano: int, duracao: int):
        super().__init__(titulo, ano)
        if duracao <= 0:
            raise ValueError("A duração deve ser positiva.")
        self.duracao = duracao

    def __str__(self):
        return f"🎬 Filme: {self.titulo} ({self.ano}) - {self.duracao} min - {self.idade} anos de lançamento"


class Livro(Midia):
    def __init__(self, titulo: str, ano: int, paginas: int):
        super().__init__(titulo, ano)
        if paginas <= 0:
            raise ValueError("O número de páginas deve ser positivo.")
        self.paginas = paginas

    def __str__(self):
        return f"📖 Livro: {self.titulo} ({self.ano}) - {self.paginas} páginas - {self.idade} anos de lançamento"


if __name__ == "__main__":
    colecao = []

    while True:
        print("\n--- Biblioteca de Mídias ---")
        print("1 - Adicionar Filme")
        print("2 - Adicionar Livro")
        print("3 - Listar Mídias")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                titulo = input("Título do filme: ")
                ano = int(input("Ano de lançamento: "))
                duracao = int(input("Duração em minutos: "))
                colecao.append(Filme(titulo, ano, duracao))
                print("Filme adicionado com sucesso!")

            elif opcao == "2":
                titulo = input("Título do livro: ")
                ano = int(input("Ano de publicação: "))
                paginas = int(input("Quantidade de páginas: "))
                colecao.append(Livro(titulo, ano, paginas))
                print("Livro adicionado com sucesso!")

            elif opcao == "3":
                print("\n--- Coleção ---")
                if not colecao:
                    print("Nenhuma mídia cadastrada.")
                for midia in colecao:
                    print(midia)

            elif opcao == "0":
                print("Saindo...")
                break

            else:
                print("Opção inválida!")

        except ValueError as e:
            print(f"Erro: {e}")
