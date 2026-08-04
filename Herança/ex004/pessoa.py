class Pessoa:
    def __init__(self, nome, idade = 0):
        self.nome = nome
        self.idade = idade
    def fazerAniversario(self):
        self.idade += 1