from rich import print
from rich.panel import Panel

class ControleRemoto:

    canal_min:int = 1
    canal_max:int = 5
    volume_min:int = 1
    volume_max:int = 5

    def __init__(self, canal = 4, volume = 2):
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

            conteudo += f"VOLUME = "
            for vol in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if vol <= self.volume_atual:
                   conteudo += f"[black on green] [/]"
                else: conteudo += f"[black on white] [/]"






        tela = Panel(conteudo, title="[ TV ]", width=32)
        print(tela)

    def liga_desliga(self):
        self.ligado = not self.ligado
    def aumenta_volume(self):
        self.volume_atual += 1
        if self.volume_atual >= ControleRemoto.volume_max:
            self.volume_atual = ControleRemoto.volume_max
    def diminuir_volume(self):
        self.volume_atual -= 1
        if self.volume_atual < ControleRemoto.volume_min:
            self.volume_atual = ControleRemoto.volume_min - 1
    def aumenta_canal(self):
        if self.canal_atual >= ControleRemoto.canal_max:
            self.canal_atual = self.canal_min
        else:
            self.canal_atual += 1

    def diminuir_canal(self):
        if self.canal_atual <= ControleRemoto.canal_min:
            self.canal_atual = self.canal_max
        else:
            self.canal_atual -= 1

tv = ControleRemoto()


while True:
    tv.mostrar_tv()
    comando = str(input(f" < CH >    - (VOL) + "))
    match comando:
        case '0':
            break
        case '@':
            tv.liga_desliga()
        case '<':
            tv.aumenta_canal()
        case '>' :
            tv.diminuir_canal()
        case '-':
            tv.diminuir_volume()
        case '+':
            tv.aumenta_volume()

