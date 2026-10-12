from .excecoes import ErroCadastro

class Partido():
    erros_validacao: int = 0
    @classmethod
    def add_erro_validacao(cls) -> None:
        cls.erros_validacao += 1

    def __init__(self, numero: str, sigla: str, nome: str, cnpj: str) -> None:
        self.numero = numero
        self.sigla = sigla
        self.nome = nome
        self.cnpj = cnpj

    @property
    def nome(self) -> str:
        return self._nome
    @nome.setter
    def nome(self, novo_nome: str) -> None:
        if len(novo_nome) <= 50:
            self._nome = novo_nome
        else:
            self.add_erro_validacao()
            raise ErroCadastro(type(self).__name__, 'nome', novo_nome)
    @property
    def cnpj(self) -> str:
        return self._cnpj
    @cnpj.setter
    def cnpj(self, novo_cnpj: str) -> None:
        if len(novo_cnpj) == 14 and novo_cnpj.isdigit():
            self._cnpj = novo_cnpj
        else:
            self.add_erro_validacao()
            raise ErroCadastro(type(self).__name__, 'cnpj', novo_cnpj)