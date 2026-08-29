from classe032 import *
from rich import print, inspect

def main():
    cc = Contabancaria(000, 'BMF', 1000)
    cc.depositar(100)
    cc.sacar(50)

    print("Tentando mudar o nome:")
    cc.nome = 'BMFZAOOOOOO'

    print(cc)




    #inspect(cc, methods= True, private=True)

if __name__ == '__main__':
    main()