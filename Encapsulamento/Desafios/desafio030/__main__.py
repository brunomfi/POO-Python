from classes030 import *

def main ():
    c = Credencial()
    c.senha = 'BMF123'
    print(c.senha)

    c.verificarSenha('BMF123')

if __name__ == '__main__':
    main()