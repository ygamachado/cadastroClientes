class Cliente():
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__divida=0

    def imprimir(self):
        print(f"|Cliente: {self.__nome} |cpf: {self.__cpf}| divida: {self.__divida}")
        print(".....................................................................")
    def valorDivida(self,divida):
        self.__divida=divida