class Avaliacao:
    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota # Atributo protected (#)

    # Criando atributo validavel
    @property
    def nota(self): #getter
        return self._nota

    @nota.setter
    def nota(self, valor): #setter
        if 0 <= valor <= 10:
            self._nota = valor
        else: print('Nota invalida, valores de 0 a 10')


    # Metodos acessores
    #def get_nota(self):
        #return self._nota

    #def set_nota(self, valor):
       # if 0 <= valor <= 10:
            #self._nota = valor
       # else:
           # print('Nota invalida, valores de 0 a 10')