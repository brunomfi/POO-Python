from rich import print
from rich.panel import Panel

class ControleRemoto:

    volume_max = 5
    volume_min = 0
    canal_max = 5
    canal_min = 1

    def __init__(self, canal = 3, volume = 2):
        self.canal_atual = canal
        self.volume_atual = volume
        self.ligado:bool = False

    def mostrarTV(self):
        conteudo = ''
        if self.ligado == False:
            conteudo += ("A TV NÃO ESTA LIGADA")
        else:
            conteudo += ("       A TV ESTA LIGADA")
            conteudo += (f"\nCANAL: [white on green]{self.canal_atual}[/]"
                         f"\nVOLUME: [white on blue]{self.volume_atual}[/]")


        tela = Panel(conteudo, title = "TV", width= 35 )
        print(tela)
    def liga_desliga(self):
        self.ligado = not self.ligado
    def diminui_canal(self):
        if self.canal_atual == self.canal_min:
            self.canal_atual = self.canal_max
        else:
            self.canal_atual -= 1
    def aumenta_canal(self):
        if self.canal_atual == self.canal_max:
            self.canal_atual = self.canal_min
        else:
            self.canal_atual += 1
    def diminuir_volume(self):

        if self.volume_atual == self.volume_min:
            self.volume_atual = self.volume_min
        else:
            self.volume_atual -= 1

    def aumentar_volume(self):
        if self.volume_atual == self.volume_max:
            self.canal_atual = self.volume_max
        else:
            self.volume_atual += 1




tv = ControleRemoto()



while True:
    tv.mostrarTV()
    comando = str(input(f"< VOL >   - CANAL + "))
    match comando:
        case '0':
            print("Desligandoooo")
            break
        case '@':
            tv.liga_desliga()
        case '<':
            tv.diminui_canal()
        case '>':
            tv.aumenta_canal()
        case '-':
            tv.diminuir_volume()
        case '+':
            tv.aumentar_volume()

