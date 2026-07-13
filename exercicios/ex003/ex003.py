class ContaBancaria:

    """
    Cria uma conta bancaria e permite fazer saques e depositos
    """

    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.nome = nome
        self.saldo = saldo
        print(f'A conta de ID: {self.id} foi criada com sucesso e o tem o saldo de : {self.saldo}')

    def __str__(self):
        return f'Conta do ID:{self.id} do {self.nome} tem R${self.saldo}'

    def deposito(self, valor):
        self.saldo += valor
        print( f'Foi feito um deposito de R$ {valor}, na CONTA de ID: {self.id} total é de R$ {self.saldo}')
    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Valor de saque de R$ {valor} é maior que o saldo, Valor INSUFICIENTE")
        else:
            self.saldo -= valor
            print(f'Foi feito um saque no valor de R$ {valor} e o valor total é de R$ {self.saldo}')

conta1 = ContaBancaria(1, 'Bruno', 3000)
conta1.deposito(45)
conta1.sacar(4000)
print(conta1)