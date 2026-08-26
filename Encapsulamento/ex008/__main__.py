from ex008 import ContaBancaria

def main():
    conta1 = ContaBancaria(111, 'BMFZAO', 5000)

    conta1.deposito(-500)
    conta1.saldo = 0
    print(conta1)


if __name__ == '__main__':
    main()