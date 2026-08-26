from email._header_value_parser import Terminal

from rich import print, inspect
from termostato import *

def main():
    t1 = Termostato()
    t1.temperatura = 25.2
    inspect(t1, private=True, methods=True)
    print(f" A temperatura atual é {t1.temperatura}")

if __name__ == '__main__':
    main()
