from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
    def darAula(self):
        print(f"O professor {self.nome} de {self.idade} Anos de idade, do {self.especialidade}, de nivel {self.nivel} começou a dar aula")

    def estudar(self):
        pass