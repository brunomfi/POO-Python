from encodings import normalize_encoding

from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    def etiqueta (self):
        print(Panel(f"[white]{self.nome} "
                    f"-------------------------------"
                    f".........R${self.preco}........."

                    ,title="Produto", style="green", width=35))

p1 = Produto("Iphone 17 Pro Max", 7890.00)
p2 = Produto("Iphone 12", 1200.00)


p1.etiqueta()
p2.etiqueta()