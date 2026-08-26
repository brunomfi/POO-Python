from rich import print
class ContaBancaria:

    """
    Cria uma conta bancaria e permite fazer saques e depositos
    """

    def __init__(self, id, nome, saldo = 0):
        self.id = id # + public
        self._nome = nome # #protect
        self.__saldo = saldo # - privado
        print(f'A conta de ID: {self.id} foi criada com sucesso e o tem o saldo de : R$ {self.__saldo}')

    def __str__(self):
        return f'Conta do ID: {self.id} do {self._nome} tem R${self.__saldo}'

    def deposito(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print( f'Foi feito um deposito de R$ {valor}, na CONTA de ID: {self.id} total é de R$ {self.__saldo}')
    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f"[bold red]Valor de saque de R$ {valor} é maior que o __saldo, Valor INSUFICIENTE[/]")
        else:
            self.__saldo -= valor
            print(f'[bold green]Foi feito um saque no valor de R$ {valor} e o valor total é de R$ {self.__saldo}[/]')

