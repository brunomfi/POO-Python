#Declaração de classes

class Nerd:
    def __init__(self):                 #Metodo Construtor
        # Atributos de Instancia
        self.nome = ''
        self.idade = 0

        # Metodo da instancia
    def aniversairo(self):
        self.idade = self.idade + 1
    def mensagem(self):
        return f'{ self.nome } é NERD e tem a {self.idade} anos de idade.'
#Declaração de Objetos

n1 = Nerd()
n1.nome = 'BRUNO'
n1.idade =  31
n1.aniversairo()
print(n1.mensagem())


n2 = Nerd()
n2.nome = 'MARCOS'
n2.idade =  34

print(n2.mensagem())
