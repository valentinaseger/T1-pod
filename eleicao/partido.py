class Partido():
    erros_validacao = 0
    @classmethod
    def erro_validacao(cls):
        cls.erros_validacao += 1

    def __init__(self, numero, sigla, nome, cnpj):
        self.numero = numero
        self.sigla = sigla
        self.nome = nome
        self.cnpj = cnpj

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) <= 50:
            self._nome = novo_nome
        else:
            self.erro_validacao()
            # colocar o que acontece se erro

    @property
    def cnpj(self):
        return self._cnpj
    @cnpj.setter
    def cnpj(self, novo_cnpj):
        if len(novo_cnpj) == 14 and novo_cnpj.isdigit():
            self._cnpj = novo_cnpj
        else:
            self.erro_validacao()
            # colocar o que acontece se erro