class ClasseSomaMultiplica:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somar(self):
        return self.a + self.b

    def multiplicar(self):
        return self.a * self.b

    def resultado(self):
        return


class ClasseDivideSubtrai(ClasseSomaMultiplica):
    def dividir(self):
        return self.a / self.b

    def subtrair(self):
        return self.a - self.b


a = ClasseDivideSubtrai(10, 20)

print(a.somar())
