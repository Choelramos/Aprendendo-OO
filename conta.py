class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("O saldo {} está na conta de {}".format(self.saldo, self.titular))

    def saca(self, valor):
        self.saldo -= valor

    def deposita(self, valor):
        self.saldo += valor
