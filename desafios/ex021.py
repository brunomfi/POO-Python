from rich import print


class Caneta:
    def __init__(self, nome):
        self.nome = nome
        self.tampada = True

    def escrever(self, msg):

        match self.nome:

            case 'azul':
                if self.tampada == False:
                    print(f"[blue]{msg}[/blue]")

                else:
                    print(f"[blue]A caneta {self.nome} está tampada[/blue]")
            case 'vermelha':
                if self.tampada == False:
                    print(f"[red]{msg}[/red]")
                else:
                    print(f"[red]A caneta {self.nome} está tampada[/red]")
            case 'verde':
                if self.tampada == False:
                    print(f"[green]{msg}[/green]")
                else:
                    print(f"[green]A caneta {self.nome} está tampada[/green]")
    def destampar(self):
            self.tampada = False

    def quebrar_linha(self, qtd=1):
        print(f"\n" * qtd, end='')


c1 = Caneta('azul')
c1.destampar()
c1.escrever('Eai galerona')


c2 = Caneta('vermelha')
c2.destampar()
c2.escrever('Eai galerona')
c2.quebrar_linha(5)


c3 = Caneta('verde')
c3.escrever('Eaiiiiiiiiiiiii')