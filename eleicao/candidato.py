from abc import ABC, abstractmethod
from .eleitor import Eleitor
from .excecoes import ErroCadastro

class Candidato(Eleitor, ABC):
    def __init__(self, nome, cpf, nascimento, titulo, zona, secao, numero, partido):
        super().__init__(nome, cpf, nascimento, titulo, zona, secao)
        self.numero = numero
        self.partido = partido
        if not self.validar_numero():
            raise ErroCadastro(type(self).__name__, 'numero', numero)

    @abstractmethod
    def validar_numero(self):
        pass