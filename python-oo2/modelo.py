class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} min'  # o '__str__' vai retornar o valor como uma string

class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporada} temporadas'

vingadores = Filme("Vingadores - guerra infinita", 2019, 160)
breakingbad = Serie("breaking bad", 2008, 5)

vingadores.dar_like()
vingadores.dar_like()
breakingbad.dar_like()

filmes_e_series = [vingadores, breakingbad]

for programa in filmes_e_series:
    print(programa)

