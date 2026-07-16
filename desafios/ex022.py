from rich import print
from rich.panel import Panel

class ControleRemoto:

    canal_min:int = 1
    canal_max:int = 6
    volume_min:int = 1
    volume_max:int = 5

    def __init__(self, canal = 3, volume = 2):
        self.canal_atual = canal
        self.volume_atual = volume
        self.ligado:bool = False
    def mostrar_tv(self):
        conteudo =''

        if self.ligado == False:

            conteudo = f'A TV não está Ligada'
        else:
            conteudo =  f"CANAL = "

            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max +  1):
                if canal == self.canal_atual:
                    conteudo += f" [yellow on yellow] {canal} [/]"
                else:
                    conteudo += f" {canal} "

        tv = Panel(conteudo, title="[ TV ]", width=35)
        print(tv)

    def liga_desliga(self):
        self.ligado = not self.ligado

tv = ControleRemoto()
tv.liga_desliga()
tv.mostrar_tv()

# f" \n< CH{self.canal_atual} >    - (VOL{self.volume_atual}) + "