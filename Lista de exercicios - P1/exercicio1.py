from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self, capacidade):
        if capacidade < 0:
            raise ValueError("Capacidade não pode ser negativa")
        self.capacidade = capacidade

    @abstractmethod
    def mover(self):
        pass

    def info(self):
        return f"Capacidade: {self.capacidade}"


class Carro(Transporte):
    def mover(self):
        return f"O carro está se movendo com até {self.capacidade} passageiros"


class Bicicleta(Transporte):
    def mover(self):
        return f"A bicicleta está se movendo com até {self.capacidade} pessoas"


if __name__ == "__main__":
    carro = Carro(5)
    bicicleta = Bicicleta(2)

    transportes = [carro, bicicleta]

    for t in transportes:
        print(t.mover())
        print(t.info())
