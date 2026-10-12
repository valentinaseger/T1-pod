from .excecoes import ErroCadastro

class Eleitor:
    def __init__(self, nome: str, cpf: str, nascimento: str, titulo: str, zona: str, secao: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = nascimento
        self.titulo_eleitor = titulo
        self.zona = zona
        self.secao = secao

    @property
    def nome(self) -> str:
        return self._nome
    @nome.setter
    def nome(self, novo_nome: str) -> None:
        if len(novo_nome) <= 50:
            self._nome = novo_nome
        else:
            raise ErroCadastro(type(self).__name__, 'nome', novo_nome)

    @property
    def cpf(self) -> str:
        return self._cpf
    @cpf.setter
    def cpf(self, novo_cpf: str) -> None:
        if len(novo_cpf) == 11 and novo_cpf.isdigit():
            self._cpf = novo_cpf
        else:
            raise ErroCadastro(type(self).__name__, 'cpf', novo_cpf)