class Urna():
    def __init__(self, zona: str | None, secao: str | None) -> None:
        self.zona = zona
        self.secao = secao
        self.votos_prefeito = {}
        self.votos_vereador = {}

    @staticmethod
    def somar_dicionarios(dic1: dict[str, int], dic2: dict[str, int]):
        nova_dic: dict[str, int] = dict(dic1)  # copia mantendo a ordem
        for chave, qtd in dic2.items():
            nova_dic[chave] = nova_dic.get(chave, 0) + qtd
        return nova_dic
    
    def __add__(self, other: 'Urna') -> 'Urna':
        nova_urna = Urna(None, None)
        nova_urna.votos_prefeito = self.somar_dicionarios(self.votos_prefeito, other.votos_prefeito)
        nova_urna.votos_vereador = self.somar_dicionarios(self.votos_vereador, other.votos_vereador)
        return nova_urna

    def registrar_voto(self, cargo: str, numero: str) -> None:
        if cargo == 'PREFEITO':
            self.votos_prefeito[numero] = self.votos_prefeito.get(numero, 0) + 1
        elif cargo == 'VEREADOR':
            self.votos_vereador[numero] = self.votos_vereador.get(numero, 0) + 1