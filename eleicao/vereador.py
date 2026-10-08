from .candidato import Candidato

class Vereador(Candidato):
    erros_validacao = 0
    @classmethod
    def erro_validacao(cls):
        cls.erros_validacao += 1

    def __init__(self, nome, cpf, nascimento, titulo, zona, secao, numero, partido, bairro, plano_governo):
        super().__init__(nome, cpf, nascimento, titulo, zona, secao, numero, partido)
        self.bairro = bairro
        self.plano_governo = plano_governo

    def validar_numero(self):
        if len(str(self.numero)) == 5:
            return True
        else:
            self.erro_validacao()
            return False