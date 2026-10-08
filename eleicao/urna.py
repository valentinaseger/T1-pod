class Urna():
    def __init__(self, zona, secao):
        self.zona = zona
        self.secao = secao
        self.votos_prefeito = {}
        self.votos_vereador = {}

    @staticmethod
    def somar_dicionarios(dic1, dic2):
        nova_dic = {}
        chaves = set(dic1) | set(dic2) # cria conjunto com as chaves
        for chave in chaves:
            nova_dic[chave] = dic1.get(chave, 0) + dic2.get(chave, 0)
        return nova_dic
    
    def __add__(self, other):
        nova_urna = Urna(None, None)
        nova_urna.votos_prefeito = self.somar_dicionarios(self.votos_prefeito, other.votos_prefeito)
        nova_urna.votos_vereador = self.somar_dicionarios(self.votos_vereador, other.votos_vereador)
        return nova_urna