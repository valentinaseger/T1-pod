class ErroCadastro(Exception):
    def __init__(self, tipo, campo, valor):
        self.tipo = tipo
        self.campo = campo
        self.valor = valor
        super().__init__(f"Erro ao cadastrar {tipo}: campo '{campo}' com valor inválido. Valor: '{valor}'")