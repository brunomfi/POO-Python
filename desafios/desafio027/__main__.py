from personagem_rpg import *


def main():

    p1 = Guerreiro('Megamen', 1000)
    p2 = Mago('Mago Negro', 2500)
    p1.atacar(p2, 200)
    p2.atacar(p1, 300)
    p2.curar()
    p1.curar()


if __name__ == '__main__':
    main()