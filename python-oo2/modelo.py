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

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'  # o '__str__' é um método doble underscore, utilizado para fazer a representação textual do objeto


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} min'


class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporada} temporadas'


class Playlist:
    def __int__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def tamanho(self):
        return len(self.programas)


vingadores = Filme("Vingadores - guerra infinita", 2019, 160)
breakingbad = Serie("breaking bad", 2008, 5)
ruptura = Serie("Ruptura", 2022, 1)
fuga = Filme("Fuga das galinhas", 1999, 100)


fuga.dar_like()
fuga.dar_like()
fuga.dar_like()
ruptura.dar_like()
ruptura.dar_like()
ruptura.dar_like()
ruptura.dar_like()
ruptura.dar_like()
vingadores.dar_like()
vingadores.dar_like()
breakingbad.dar_like()


filmes_e_series = [vingadores, breakingbad, ruptura, fuga]

playlist_fim_de_semana = Playlist("fim_de_semana", filmes_e_series)

for programa in playlist_fim_de_semana.programas:
    print(programa)

