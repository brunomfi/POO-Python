from rich import print, inspect

from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():
    a1 = Aluno('BMF', 31, 'ADS', 'T01')
    a1.fazerMatricula()
    a1.fazerAniversario()
    inspect(a1, methods=True)

    p1 = Professor('Guanabara', 45, 'Curso em Video', 'Mestrado')
    p1.fazerAniversario()
    inspect(p1, methods=True)

if __name__ == "__main__":
    main()