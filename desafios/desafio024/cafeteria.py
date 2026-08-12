from abc import ABC, abstractmethod
from xml.etree.ElementPath import prepare_parent


class BebidaQuente(ABC):
    def __init__(self):
        pass
    def preparar(self):
        print(f""" INCIANDO PREPARO
        1.{(self.ferver_agua())}
        2.{(self.misturar())}
        3.{(self.servir())}
    FIM 

""")
    def ferver_agua(self):
        return f" Fervendo agua a 100ºC. "
    @abstractmethod
    def misturar(self):
        pass
    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):

    def misturar(self):
        return f" Passando agua pressurizada pelo pó do cafe moído."
    def servir(self):
        return f" Servindo em xicará pequena."

class Cha(BebidaQuente):

    def misturar(self):
        return f" Mergulhando o CHA na agua quente."
    def servir(self):
        return f" Servindo em xicará de Chá."
class Leite(BebidaQuente):

    def misturar(self):
        return f" Colocando pó de leite desnatado na agua quente."
    def servir(self):
        return f" Servindo Leite no copo grande."













