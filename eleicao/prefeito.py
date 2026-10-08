from .candidato import Candidato

class Prefeito(Candidato):
    erros_validacao = 0
    @classmethod
    def erro_validacao(cls):
        cls.erros_validacao += 1

    def __init__(self, nome, cpf, nascimento, titulo, zona, secao, numero, partido, cpf_vice, plano_governo):
        super().__init__(nome, cpf, nascimento, titulo, zona, secao, numero, partido)
        self.cpf_vice = cpf_vice
        self.plano_governo = plano_governo

    def validar_numero(self):
        if len(str(self.numero)) == 2:
            return True
        else:
            self.erro_validacao()
            return False

    @property
    def cpf_vice(self):
        return self._cpf_vice

    @cpf_vice.setter
    def cpf_vice(self, novo_cpf):
        if len(novo_cpf) == 11 and novo_cpf.isdigit():
            self._cpf_vice = novo_cpf
        else:
            pass # tratar erro