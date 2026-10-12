from .candidato import Candidato
from .excecoes import ErroCadastro
from .partido import Partido

class Prefeito(Candidato):
    erros_validacao = 0
    @classmethod
    def add_erro_validacao(cls):
        cls.erros_validacao += 1

    def __init__(self, nome: str, cpf: str, nascimento: str, titulo: str, zona: str, secao: str, numero: str, partido: Partido, cpf_vice: str, plano_governo: str) -> None:
        super().__init__(nome, cpf, nascimento, titulo, zona, secao, numero, partido)
        self.cpf_vice = cpf_vice
        self.plano_governo = plano_governo

    def validar_numero(self) -> bool:
        if len(str(self.numero)) == 2 and str(self.numero).isdigit():
            return True
        else:
            self.add_erro_validacao()
            return False

    @property
    def cpf_vice(self) -> str:
        return self._cpf_vice

    @cpf_vice.setter
    def cpf_vice(self, novo_cpf: str) -> None:
        if len(novo_cpf) == 11 and novo_cpf.isdigit():
            self._cpf_vice = novo_cpf
        else:
            raise ErroCadastro(type(self).__name__, 'cpf_vice', novo_cpf)