from abc import ABC, abstractmethod


class Time:
    def __init__(self, nome_time: str, cidade: str, nome_mascote: str):
        self.nome_time = nome_time
        self.cidade = cidade
        self.nome_mascote = nome_mascote


class Jogador:
    def __init__(self, nome: str, time: Time, num_camisa: int):
        self.nome = nome
        self.time = time
        self.num_camisa = num_camisa


class Comissao(ABC):
    def __init__(self, nome_profissional: str, time: Time):
        self.nome_profissional = nome_profissional
        self.time = time

    @abstractmethod
    def dar_coletiva(self):
        pass


class Tecnico(ABC, Comissao):
    def __init__(self, nome: str, time: Time, esquema_tatico: tuple):
        super().__init__(nome, time)
        self.esquema_tatico = esquema_tatico

    def dar_coletiva(self):
        return (f'O técnico {self.nome_profissional}, '
                f'do time {self.time.nome_time}, está dando uma coletiva de imprensa.')


class Auxiliar(ABC, Comissao):
    def __init__(self, nome: str, time: Time, esquema_tatico: tuple):
        super().__init__(nome, time)
        self.esquema_tatico = esquema_tatico

    def dar_coletiva(self):
        return (f'O auxiliar técnico {self.nome_profissional}, '
                f'do time {self.time.nome_time}, está dando uma coletiva de imprensa.')


class PreparadorFisico(ABC, Comissao):
    def __init__(self, nome: str, time: Time, parte_elenco: str):
        super().__init__(nome, time)
        self.parte_elenco = parte_elenco

    def dar_coletiva(self):
        return (f'O preparador físico {self.nome_profissional}, '
                f'do time {self.time.nome_time}, está dando uma coletiva de imprensa.')


