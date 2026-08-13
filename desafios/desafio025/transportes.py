from abc import ABC, abstractmethod

class Transporte(ABC):

    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):

    fator = 0.50

    def calc_frete(self):
        return f'R$ {self.fator * self.distancia}'

class Caminhao(Transporte):
    fator = 1.20
    def calc_frete(self):
        if self.distancia < 50:
            return f'Não é possivel fazer, menor que 50km'
        else:
            return f'R$ {self.fator * self.distancia}'

class Drone(Transporte):
    fator = 9.50
    def calc_frete(self):
        if self.distancia > 5:
            return f'Não é possivel fazer, até 10km'
        else:
            return f'R$ {self.fator * self.distancia}'
