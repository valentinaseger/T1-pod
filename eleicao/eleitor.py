class Eleitor:
    def __init__(self, nome, cpf, nascimento, titulo, zona, secao):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = nascimento
        self.titulo_eleitor = titulo
        self.zona = zona
        self.secao = secao

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) <= 50:
            self._nome = novo_nome
        else:
            pass # colocar o que acontece caso erro

    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, novo_cpf):
        if len(novo_cpf) == 11 and novo_cpf.isdigit():
            self._cpf = novo_cpf
        else:
            pass # colocar o que acontece caso erro