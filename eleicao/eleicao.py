from .prefeito import Prefeito
from .vereador import Vereador
from .urna import Urna

class Eleicao():
    def __init__(self):
        self.eleitores = []
        self.partidos = []
        self.urnas = []

    def inserir_eleitore(self, eleitor):
        self.eleitores.append(eleitor)
    def inserir_partido(self, partido):
        self.partidos.append(partido)
    def inserir_urna(self, urna):
        self.urnas.append(urna)

    def buscar_eleitor(self, titulo_eleitor):
        for eleitor in self.eleitores:
            if eleitor.titulo_eleitor == titulo_eleitor:
                return eleitor
        return None
    def buscar_candidato(self, numero, tipo):
        for eleitor in self.eleitores:
            if tipo == 'prefeito' and isinstance(eleitor, Prefeito) and eleitor.numero == numero:
                return eleitor
            if tipo == 'vereador' and isinstance(eleitor, Vereador) and eleitor.numero == numero:
                return eleitor
        return None
    def buscar_partido(self, numero):
        for partido in self.partidos:
            if partido.numero == numero:
                return partido
        return None
    def buscar_urna(self, zona, secao):
        for urna in self.urnas:
            if urna.zona == zona and urna.secao == secao:
                return urna
        return None

    def unifica_urnas(self):
        urna_unificada = Urna(None, None)
        for urna in self.urnas:
            urna_unificada = urna_unificada + urna
        return urna_unificada

    def contar_votos(self, dict_votos, tipo_candidato, tipo_voto):
        brancos = 0
        nulos = 0
        validos = 0
        for num_candidato, qtd_votos in dict_votos.items():
            if num_candidato == "":
                brancos += qtd_votos
            elif self.buscar_candidato(num_candidato, tipo_candidato) == None:
                nulos += qtd_votos
            else:
                validos += qtd_votos
        if tipo_voto == 'branco':
            return brancos
        elif tipo_voto == 'nulo':
            return nulos
        else:
            return validos


    def relatorio_eleitores(self):
        total_eleitores = len(self.eleitores)

        canditados_prefeito = 0
        candidatos_vereador = 0
        for eleitor in self.eleitores:
            if isinstance(eleitor, Prefeito):
                canditados_prefeito += 1
            elif isinstance(eleitor, Vereador):
                candidatos_vereador += 0

        texto_final = '========== ELEITORES ==========\n\n' \
                f'Total de eleitores: {total_eleitores}\n' \
                f'Total de canditados a prefeito: {canditados_prefeito}\n' \
                f'Total de canditados a vereador: {candidatos_vereador}\n\n'

        dic_zonas = {}
        for eleitor in self.eleitores:
            zona = eleitor.zona
            secao = eleitor.secao

            if not(zona in dic_zonas):
                dic_zonas[zona] = {}
            if not(secao in dic_zonas[zona]):
                dic_zonas[zona][secao] = 0
            dic_zonas[zona][secao] += 1

        for zona, secoes in dic_zonas.items():
            string = f'\n----- Zona {zona}\n'
            for secao, qtd in secoes.items():
                string += f'---------- Seção {secao}: {qtd} eleitores\n'
            texto_final += string

        return texto_final + '\n\n\n'
    
    def relatorio_partidos(self):
        total_partidos = len(self.partidos)

        texto_final = '========== PARTIDOS ==========\n\n' \
                f'Total de partidos: {total_partidos}\n\n'

        for partido in self.partidos:
            qtd_prefeito = 0
            qtd_vereador = 0
            for eleitor in self.eleitores:
                if isinstance(eleitor, Prefeito) and eleitor.partido == partido:
                    qtd_prefeito += 1
                if isinstance(eleitor, Vereador) and eleitor.partido == partido:
                    qtd_vereador += 1

            texto_final += f'\n----- Partido {partido.nome}\n' \
                            f'---------- Sigla: {partido.sigla}\n' \
                            f'---------- Número de candidatos a prefeito: {qtd_prefeito}\n' \
                            f'---------- Número de candidatos a vereador: {qtd_vereador}\n' \

        return texto_final + '\n\n\n'
    
    def relatorio_urnas(self):
        texto_final = '========== URNAS ==========\n\n'
        cont_urnas = 0
        for urna in self.urnas:
            cont_urnas += 1
            tipo_candidato = 'prefeito'
            qtd_validos_prefeito = self.contar_votos(urna.votos_prefeito, tipo_candidato, 'valido')
            qtd_nulos_prefeito = self.contar_votos(urna.votos_prefeito, tipo_candidato, 'nulo')
            qtd_brancos_prefeito = self.contar_votos(urna.votos_prefeito, tipo_candidato, 'branco')

            tipo_candidato = 'vereador'
            qtd_validos_vereador = self.contar_votos(urna.votos_vereador, tipo_candidato, 'valido')
            qtd_nulos_vereador = self.contar_votos(urna.votos_vereador, tipo_candidato, 'valido')
            qtd_brancos_vereador = self.contar_votos(urna.votos_vereador, tipo_candidato, 'valido')

            texto_final += f'----- Urna {cont_urnas}\n' \
                            f'---------- Zona {urna.zona}\n' \
                            f'---------- Seção {urna.secao}\n' \
                            f'---------- Votos para prefeito: \n' \
                            f'--------------- Válidos: {qtd_validos_prefeito}\n' \
                            f'--------------- Nulos: {qtd_nulos_prefeito}\n' \
                            f'--------------- Brancos: {qtd_brancos_prefeito}\n' \
                            f'---------- Votos para vereador: \n' \
                            f'--------------- Válidos: {qtd_validos_vereador}\n' \
                            f'--------------- Nulos: {qtd_nulos_vereador}\n' \
                            f'--------------- Brancos: {qtd_brancos_vereador}\n'
            

        return texto_final + '\n\n\n'
    def relatorio_geral(self):
        # nome dos 10 vereadores com a maior quantidade de votos (e o número de votos)
        
        texto_final = '========== Relatório de resultado geral =========='

        urna_unificada = self.unifica_urnas()
        total_votos_validos_prefeito = self.contar_votos(urna_unificada, 'prefeito', 'valido')
        votos_prefeito_ordenados = dict(sorted(urna_unificada.votos_prefeito.items(), key=lambda item: item[1], reverse=True))
        if next(iter(votos_prefeito_ordenados.values())) > (total_votos_validos_prefeito / 2):
            texto_final += f'Prefeito eleito: {next(iter(votos_prefeito_ordenados))}\n\n'
        else:
            texto_final += 'Necessita de segundo turno para prefeito\n\n'

        votos_vereador_ordenados = dict(sorted(urna_unificada.votos_vereador.items(), key=lambda item: item[1], reverse=True))
        vereadores = list(votos_vereador_ordenados)[:10]
        for vereador in vereadores:
            texto_final += f'{vereador}: {votos_vereador_ordenados[vereador]} votos' # se tiver dois com o mesmo nome? teria que buscar pelo número? a chave em urna é o número ou nome?
        
            
    def relatorio_erros(self):
        # informa cada mensagem gerada pelas classes de erro
        # informar os valores dos atributos que contabilizam os erros nas classes 'Partido', 'Prefeito' e 'Vereador'
        pass