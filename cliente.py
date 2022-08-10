class Cliente():
    def __init__(self, nome: object, cpf: object, idade: object, endereco: object) -> object:
        self.__nome = nome
        self.__cpf = cpf
        self.__divida=0
        self.__idade=int(idade)
        self.__endereco = endereco

    def imprimir(self):
        print(f"|Cliente: {self.__nome} |cpf: {self.__cpf}|endereco: {self.__idade}| divida: {self.__divida}")
        print(".....................................................................")
    def valorDivida(self,divida):
        self.__divida=divida

#mudança