from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas



    def avancar(self, valor):
        print(f'Você acabou de abrir o Livro: {self.titulo} contem: {self.paginas} Páginas')

        i = 0
        while i < self.paginas:
            print(f"Pag{i+1} ", end='')
            #sleep(1)
            i += 1
            if valor == i:
                self.paginas -= valor
                break





l1 = Livro("Protocolo", 20)
l1.avancar(5)
