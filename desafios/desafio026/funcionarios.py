from abc import ABC, abstractmethod
from rich.table import Table

class Funcionario(ABC):

    sal_min = 1621
    desconto_inss = 7.5


    def __init__(self, nome = None ):
        self.nome = nome
        self.salarioBruto = 0
        self.salario = 0

    @abstractmethod
    def calc_salario(self):
        pass

    def analisar_salario(self):
        pass


class FuncionarioHorista(Funcionario):

    def __init__(self, nome = None, valor_hora= 0, qtd_hora= 220 ):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.qtd_hora = qtd_hora

    def calc_salario(self):
        self.salario = self.valor_hora * self.qtd_hora
        self.salarioBruto = self.salario - ( self.salario * (self.desconto_inss /100))

    def analisar_salario(self):
        return self.salarioBruto / self.sal_min

class FuncionarioMensalista(Funcionario):
    def calc_salario(self):
        pass