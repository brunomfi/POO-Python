from rich.panel import Panel
from rich import print

class Churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant
    def analisar(self):
        print(Panel(f"Analisando o [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]"
                    f"Cada participante comerá 0.4Kg e cada Kg custá valor de R$ 82,40"
                    f""
                    ,


                    title= self.titulo, ))

c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()