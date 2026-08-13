from rich import print, box

from transportes import *
from rich.table import Table

def main():
    dist = 55
    """entrega = Caminhao(dist)
    print(f'Frete de {type(entrega).__name__} em {dist}Km = {entrega.calc_frete()}')"""

    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

    tabela = Table(title="Tabelas de frete")
    tabela.add_column("Distancia")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")

    for item in viagem:
        tabela.add_row(f"{dist}Km", f"{type(item).__name__}", f"{item.calc_frete()}")

    print(tabela)
if __name__ == '__main__':
    main()