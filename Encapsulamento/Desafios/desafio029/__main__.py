from diario import *
from rich import inspect
def main():
    d = Diario('Doidemais')
    d.escrever('Tem dias que são noites')
    d.escrever('Não é predio Edificio')
    d.ler('Doidemais')
    inspect(d, private=True, methods=True)




if __name__ == "__main__":
    main()
