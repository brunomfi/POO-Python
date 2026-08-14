from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

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
        mensagem = (f"O salario de [blue]{self.nome}[/blue] [purple]({self.__class__.__name__})[/purple], corresponde ao valor de [green]{self.salarioBruto:.2f}[/green],"
                    f" corresponde ao valor de [yellow]{self.salarioBruto/self.sal_min:.2f}[/yellow] salarios minimos")
        painel = Panel(mensagem, title='Analise do Salario', width=50)
        print(painel)

class FuncionarioHorista(Funcionario):

    def __init__(self, nome = None, valor_hora= 0, qtd_hora= 220 ):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.qtd_hora = qtd_hora

    def calc_salario(self):
        self.salario = self.valor_hora * self.qtd_hora
        self.salarioBruto = self.salario - ( self.salario * (self.desconto_inss /100))




class FuncionarioMensalista(Funcionario):

    def __init__(self, nome = None, salario= 0):
        super().__init__(nome)
        self.salario= salario


    def calc_salario(self):
        self.salarioBruto = self.salario - self.salario * (self.desconto_inss /100)