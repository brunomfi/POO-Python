import random
from abc import ABC, abstractmethod
from rich import print
from random import randint

class Personagem(ABC):

    def __init__(self, nome = None, vida = 0):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca):
        if alvo.vida > 0 and self.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f'O [green]{self.nome}[/],({self.vida}) atacou o [red]{alvo.nome}[/] ({alvo.vida}), com um [yellow]{golpe}[/] de {forca} ')
            alvo.receber_dano(forca)
        else:
            print(f'O ataque de {self.nome} em {alvo.nome} não foi possivel ser feito ')

    def receber_dano(self, dano):
        fator = randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu dano de {fator}, ficando com vida de {self.vida}")


    @abstractmethod
    def curar(self):
        pass



class Guerreiro(Personagem):
    def __init__(self, nome = None, vida = 0):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Golpe de Machado", "Pulo giratorio"]

    def curar(self):
        fator = randint(0, 100)
        self.vida += fator
        print(f'O personagem [blue]{self.nome}[/blue] recebeu cura de {fator} e a vida de total de {self.vida}')

class Mago(Personagem):
    def __init__(self, nome = None, vida = 0):
        super().__init__(nome, vida)
        self.golpes = ["Bola de fogo", "Raio de Luz", "Magia Estática"]

    def curar(self):
        fator = randint(0, 100)
        self.vida += fator
        print(f'O personagem [blue]{self.nome}[/blue] recebeu cura de {fator} e a vida de total de {self.vida}')