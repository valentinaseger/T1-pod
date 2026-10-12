from abc import ABC, abstractmethod
from .eleitor import Eleitor
from .excecoes import ErroCadastro
from .partido import Partido

class Candidato(Eleitor, ABC):
    def __init__(self, nome: str, cpf: str, nascimento: str, titulo: str, zona: str, secao: str, numero: str, partido: Partido) -> None:
        super().__init__(nome, cpf, nascimento, titulo, zona, secao)
        self.numero = numero
        self.partido = partido
        if not self.validar_numero():
            raise ErroCadastro(type(self).__name__, 'numero', numero)

    @abstractmethod
    def validar_numero(self) -> bool:
        pass