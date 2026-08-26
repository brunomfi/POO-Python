from rich import print, inspect
from abc import ABC, abstractmethod

class Termostato:

    def __init__(self, temperatura = 24):

        self.__temperatura = temperatura

    @property
    def ftemperatura(self):
        return f'{self.__temperatura}ºC'

    @property
    def temperatura(self):
        return self.__temperatura
    @temperatura.setter
    def temperatura(self, valor):
        if valor % 0.5 != 0:
            raise ValueError(f"Temperatura invalida: {valor}")

        if valor <= 16:
            self.__temperatura = 16
        elif valor >= 30:
            self.__temperatura = 30
        print(self.temperatura)