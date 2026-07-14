from rich.panel import Panel
from rich import print

class Churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant
    def analisar(self):
        totalkg = self.quant * 0.40
        cadaP = totalkg * 82.40
        print(Panel(f""
                    f"Analisando o [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]"
                    f"\nCada participante comerá 0.4Kg e cada Kg custá valor de R$ 82,40"
                    f"\nÉ recomendado comprar [green]{totalkg}Kg[/] de carne"
                    f"\nO custo total será [yellow]R$ {cadaP:.2f}[/]"
                    f"\nCada pessoa deverá pagar R$ [yellow]R$ {cadaP / self.quant:.2f}[/]"
                    ,


                    title= self.titulo, width=70 ))

c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()