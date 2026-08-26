

class Diario:
    def __init__(self, senha = 'LoucuraDemais'):
        self.__senha = senha
        self.__segredos = []


    def escrever(self, msg):
        self.__segredos.append(msg)
    def ler(self, senha= None):
        if senha == self.__senha:
            for segredos in self.__segredos:
                print(f' - {segredos}')
        else:
            raise PermissionError('Senha incorreta')


