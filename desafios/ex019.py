from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(
            f'[blue]Você acabou de abrir o Livro: [red]{self.titulo}[/] contem: [green]{self.paginas} Páginas no total[/]'
            f'\nVocê agora está na [yellow]Pagina {self.pagina_atual}[/]')

    def avancar(self, valor):

            i = 1
            while i < valor+1 :
                print(f"Pag{self.pagina_atual+ 1}, ", end='')
                sleep(0)
                i += 1
                self.pagina_atual += 1
                if valor + 1 == i:
                    print(f'Você avançou {i-1} paginas e está na pagina {self.pagina_atual}, restam {i-2} paginas')
                    break

                if self.pagina_atual == self.paginas:
                    print(
                        f'Você avançou {i - 1} paginas e está na pagina {self.pagina_atual}, restam {self.paginas - self.paginas} paginas')
                    print(f'[red] Você chegou ao final do livro [green]{self.titulo}[/]')
                    break

l1 = Livro("BMF EM PROTOCOLO", 20)
l1.avancar(10)
l1.avancar(5)
l1.avancar(50)