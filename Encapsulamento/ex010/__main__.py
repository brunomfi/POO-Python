from rich import print, inspect

from ex010 import Avaliacao







def main():
    av1 = Avaliacao('BMF', "Algoritimos Geneticos")
    av1.nota = 5

    inspect(av1, private=True)


if __name__ == '__main__':
    main()