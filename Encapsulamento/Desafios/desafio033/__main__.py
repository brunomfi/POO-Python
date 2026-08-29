from classes033 import *

def main():
    a1 = Aluno('BMF', 1994)

    a1.add_curso('info')
    print(a1.curso_oficiais)
    a1.curso = 'info'






    print(a1.__dict__)

if __name__ == '__main__':
    main()