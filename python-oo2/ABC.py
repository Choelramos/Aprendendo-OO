# Testando o ABC de modo que ninguém consiga
# instanciar um objeto da classe Programa
# e será necessário implementar o __str__ nas subclasses

from abc import ABCMeta, abstractmethod


class Programa(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self):
        pass