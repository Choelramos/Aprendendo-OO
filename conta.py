class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo {} está na conta de {}".format(self.__saldo, self.__titular))

    def saca(self, valor):
        self.__saldo -= valor

    def deposita(self, valor):
        self.__saldo += valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def get_titular(self):
        return self.__titular

    def set_limite(self, limite):
        self.__limite = limite



