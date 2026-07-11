#Declaração de classes

class Nerd:
    def __init__(self,n = 'Vazio', i =0 ):                 #Metodo Construtor
        # Atributos de Instancia
        self.nome = n
        self.idade = i

        # Metodo da instancia
    def aniversairo(self):
        self.idade = self.idade + 1
    def mensagem(self):
        return f'{ self.nome } é NERD e tem a {self.idade} anos de idade.'
    def __str__(self):
        return f'{self.nome} é NERD e tem a {self.idade} anos de idade.'

    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade} '
#Declaração de Objetos

n1 = Nerd('Bruno', 31)
n1.aniversairo()
#print(n1)
print(n1.__dict__)
print(n1.__getstate__())
print(n1.__class__) 
n2 = Nerd('Marcos', 34)
print(n2)


n3 = Nerd()
print(n3)
