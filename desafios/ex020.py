from shutil import which

from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self,nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()
    def favorito(self, game):
        self.favoritos.append(game)

    def ficha(self):
        # Aqui cria um atributo de conteudo para ser exibido dentro da ficha, fizemos um for para percorer cada game adicionado.
        conteudo = ''
        for num, game in enumerate(self.favoritos):
            conteudo += f'\n:video_game:[blue] {game}[/]'

        print(Panel(f"Nome real: {self.nome}"
                    f"\nNick: {self.nick}"
                    f"\nJogos Favoritos:"
                    f"{conteudo}"
                    ,
                    title= f"Jogador <{self.nick}>", width=45  ))
g1 = Gamer("Bruno Medeiros", "BMF")
g1.favorito("Mortal Kombat")
g1.favorito("Super Mario")
g1.ficha()