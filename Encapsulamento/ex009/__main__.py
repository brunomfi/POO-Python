from rich import print, inspect

from ex009 import Avaliacao


def main():
    av1 = Avaliacao('BMF', "Algoritimos Geneticos")
    av1.set_nota(11)

    inspect(av1, private=True)


if __name__ == '__main__':
    main()