from abc import ABC, abstractmethod # Abstract Base Classes

class Pessoa(ABC):
    def __init__(self, nome, idade = 0):
        self.nome = nome
        self.idade = idade
    def fazerAniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass