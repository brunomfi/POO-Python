from rich.panel import Panel
from rich import print

class Churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant
    def analisar(self):
        print(Panel(f"\nAnalisando o [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]"
                    f"\nCada participante comerá 0.4Kg e cada Kg custá valor de R$ 82,40"
                    f"\nÉ recomendado comprar {0.4*self.quant}Kg de carne"
                    ,


                    title= self.titulo, width=70 ))

c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()