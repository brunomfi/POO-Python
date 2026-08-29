from abc import ABC,abstractmethod
import datetime

class Pessoa(ABC):
    def __init__(self,nome, nasc):

        self._nome = nome
        self._nasc = nasc


    @property
    def idade(self):
        return 2026-self._nasc

    @idade.setter
    def idade(self,valor):
        raise PermissionError ("Você não pode alterar a idade. Mude o ano de nascimento")

class Aluno(Pessoa):
    curso_oficiais = ["ADS", "ADM"]

    def __init__(self,nome,nasc, curso = ''):
        super().__init__(nome,nasc)
        self._curso = curso



    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, valor):
        for v in self.curso_oficiais:
            if valor not in self.curso_oficiais:
                raise ValueError(f"o curso : {v}, não está nos Cursos oficiais")

            else:
                self._curso = v


    def add_curso(self,valor):
        if valor not in self.curso_oficiais:
            self.curso_oficiais.append(valor)

        else:
            raise ValueError (f'Curso {valor} já existe em Cursos Oficiais')












