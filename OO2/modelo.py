class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    def __str__(self):
        return f'Nome: {self.nome} - Ano:  {self.ano} Likes: {self.likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - Ano:  {self.ano} - Duracão:{self.duracao}Min Likes: {self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - Ano:  {self.ano} - Temporadas:{self.temporadas} Likes: {self.likes}'


class playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo Mundo em panico', 1999, 100)
demolido = Serie('Demolidor', 2016, 2)

demolido.dar_likes()
demolido.dar_likes()
demolido.dar_likes()
vingadores.dar_likes()
tmep.dar_likes()
vingadores.dar_likes()
tmep.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta, tmep, demolido]
playlist_fim_de_semana = playlist('Fim de semana', filmes_e_series)

for programa in playlist_fim_de_semana:
    print(programa)
