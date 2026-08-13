from rich import print

from transportes import *


def main():
    dist = 5
    entrega = Caminhao(dist)
    print(f'Frete de {type(entrega).__name__} em {dist}Km = {entrega.calc_frete()}')

if __name__ == '__main__':
    main()