from abc import ABC, abstractmethod
from .eleitor import Eleitor

class Candidato(Eleitor, ABC):
    def __init__(self, nome, cpf, nascimento, titulo, zona, secao, numero, partido):
        super().__init__(nome, cpf, nascimento, titulo, zona, secao)
        self.numero = numero
        self.partido = partido

    @abstractmethod
    def validar_numero(self):
        pass