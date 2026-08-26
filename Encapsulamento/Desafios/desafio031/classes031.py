

class Retangulo:
    def __init__(self, base= 1 , altura = 1):

        self._base = None
        self._altura = None
        self._area = None

        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError ("O valor deve ser um numero")
        if valor < 0:
            raise ValueError("O valor invalido para base")
        else:
            self._base = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("O valor deve ser um numero")
        if valor < 0:
            raise ValueError("O valor invalido para base")
        else:
            self._altura = valor

    @property
    def area(self):
        self._area = self._altura * self._base
        return self._area
    @area.setter
    def area(self):
        raise PermissionError ("Area não pode ser configurada")
    @property
    def medidas(self):
        return (f'Base = {self._base} '
                f'\nAltura = {self.altura}'
                f'\nArea = {self.area}')
    @medidas.setter
    def medidas(self, valores:tuple):
        if not isinstance(valores, tuple):
            raise TypeError ("O valor deve ser em tupla")
        if len(valores) != 2:
            raise TypeError ("O valor deve ser em  dois valores numericos")
        if isinstance(valores[0], float) and isinstance(valores[0], int):
            self.base = valores[0]
        if isinstance(valores[1], float) and isinstance(valores[1], int):
            self.altura = valores[1]



        else:
            raise TypeError ("O valor deve ser um numero")




