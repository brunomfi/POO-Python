from rich import print
class Funcionario:
    def __init__(self,nome, setor, cargo, empresa = 'Apper Software'):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = empresa
    def apresentacao(self):
        print( f':partying_face: Olá, sou [blue]{self.nome}[/], e sou {self.cargo} do setor {self.setor} da empresa {self.empresa}')


c1 = Funcionario("Bruno", "TI", "Programador")
c1.apresentacao()