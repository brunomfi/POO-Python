
from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
    def baterPonto(self):
        print(f" Funcioario(a): {self.nome} acabou de bater o ponto")