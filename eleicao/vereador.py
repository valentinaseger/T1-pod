from .candidato import Candidato
from .partido import Partido

class Vereador(Candidato):
    erros_validacao = 0
    @classmethod
    def add_erro_validacao(cls):
        cls.erros_validacao += 1

    def __init__(self, nome: str, cpf: str, nascimento: str, titulo: str, zona: str, secao: str, numero: str, partido: Partido, bairro: str, projeto_lei: str):
        super().__init__(nome, cpf, nascimento, titulo, zona, secao, numero, partido)
        self.bairro = bairro
        self.projeto_lei = projeto_lei

    def validar_numero(self) -> bool:
        if len(str(self.numero)) == 5 and str(self.numero).isdigit():
            return True
        else:
            self.add_erro_validacao()
            return False