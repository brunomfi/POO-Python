import hashlib
from hashlib import sha256
from pwinput import pwinput

class Contabancaria():



    def __init__(self, id = 1, titular = '', saldo = 0, chave:str = None ):

        self._id = None
        self._titular = None
        self.__saldo = None
        if chave is None:
            chave = self.pede_senha()
        self.__hash = self.__hash = sha256(chave.encode('utf-8')).hexdigest()

        self.id = id
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f'Conta do ID: {self.id} do {self.titular} tem R${self.__saldo}'

    def pede_senha(self) -> str:
        while True:

            senha = str(pwinput('Digite sua senha: '))
            if len(senha) >= 6:
                break
        return senha
    def validar_senha(self, chave) -> bool:
        usuario = hashlib.sha256(chave.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False



    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, valor):
        self._id = valor


    @property
    def titular(self):
        return self._titular
    @titular.setter
    def titular(self, valor):
        self._titular = valor

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, valor ):

            if valor >= 0:

                self.__saldo = valor
            else:
                raise ValueError('Saldo invalido')
    @property
    def nome(self):
        return self._titular
    @nome.setter
    def nome(self, novoNome:str = None):
        chave = self.pede_senha()

        if self.validar_senha(chave):
            self._titular = novoNome
        else:
            print('Senha invalida')



    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Feito deposito de R$ {valor} valor total de: R${self.saldo}')
        else:
            raise ValueError('Valor invalido')

    def sacar(self, valor,chave:str = None ):
        if chave is None:
            chave = self.pede_senha()

        if self.validar_senha(chave):
            if valor <= self.saldo:
                self.saldo -= valor
                print(f'Feito saque de R${valor} restante de: R${self.saldo}')
            else:
                print(f'Saldo: {self.saldo}')
                raise ValueError('Saque indisponivel, valor menor que saldo')







