from funcionarios import *

def main():
   f1 = FuncionarioHorista('BMF', 11.36, 176)
   f1.calc_salario()
   f1.analisar_salario()

   f2 = FuncionarioMensalista('BRUNÃO', 2500)
   f2.calc_salario()
   f2.analisar_salario()

if __name__ == '__main__':
    main()