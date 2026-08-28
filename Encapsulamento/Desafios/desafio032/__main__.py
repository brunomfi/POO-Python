from classe032 import *
from rich import print, inspect

def main():
    cc = Contabancaria(000, 'BMF', 1000)
    cc.depositar(100)


    #inspect(cc, methods= True, private=True)

if __name__ == '__main__':
    main()