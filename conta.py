class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo {} está na conta de {}".format(self.__saldo, self.__titular))

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_para_saque = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_para_saque

    def __saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} é maior que seu saldo!".format(self.__pode_sacar(valor)))

    def deposita(self, valor):
        self.__saldo += valor

    def transfere(self, valor, destino):
        self.__saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter    #  aqui estamos usando o get, usando o property
    def limite(self, limite):
        self.__limite = limite



