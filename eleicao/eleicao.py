from .prefeito import Prefeito
from .vereador import Vereador
from .urna import Urna

class Eleicao():
    def __init__(self):
        self.eleitores = []
        self.partidos = []
        self.urnas = []

    def inserir_eleitor(self, eleitor):
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

    def filtra_validos(self, votos, tipo):
        # retorna os votos dos candidatos, sem votos nulos e brancos
        filtrado = {}
        for candidato, qtd in votos.items():
            if candidato == "":
                pass
            elif self.buscar_candidato(candidato, tipo) == None:
                pass
            else:
                filtrado[candidato] = qtd
        return filtrado

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

        candidatos_prefeito = 0
        candidatos_vereador = 0
        for eleitor in self.eleitores:
            if isinstance(eleitor, Prefeito):
                candidatos_prefeito += 1
            elif isinstance(eleitor, Vereador):
                candidatos_vereador += 1

        texto_final = '========== ELEITORES ==========\n\n' \
                f'Total de eleitores: {total_eleitores}\n' \
                f'Total de candidatos a prefeito: {candidatos_prefeito}\n' \
                f'Total de candidatos a vereador: {candidatos_vereador}\n\n'

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
            qtd_nulos_vereador = self.contar_votos(urna.votos_vereador, tipo_candidato, 'nulo')
            qtd_brancos_vereador = self.contar_votos(urna.votos_vereador, tipo_candidato, 'branco')

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
        validos_prefeito = self.filtra_validos(urna_unificada.votos_prefeito, 'prefeito')
        total_votos_validos_prefeito = sum(validos_prefeito.values())

        ranking_prefeito = sorted(validos_prefeito.items(), key=lambda item: item[1], reverse=True)

        if len(ranking_prefeito) == 0:
            texto_final += 'Nenhum voto válido para prefeito\n'
        else:
            numero_vencedor, votos_vencedor = ranking_prefeito[0]
            if votos_vencedor >= total_votos_validos_prefeito / 2:
                prefeito = self.buscar_candidato(numero_vencedor, 'prefeito')
                texto_final += f'Prefeito eleito: {prefeito.nome}\n'
            else:
                texto_final += 'Segundo Turno\n'

        validos_vereador = self.filtra_validos(urna_unificada.votos_vereador, 'vereador')
        ranking_vereador = sorted(validos_vereador.items(), key=lambda item: item[1], reverse=True)

        for numero, votos in ranking_vereador[:10]:
            vereador = self.buscar_candidato(numero, 'vereador')
            texto_final += f'{vereador.nome}: {votos} votos\n'

        return texto_final
        
            
    def relatorio_erros(self):
        # informa cada mensagem gerada pelas classes de erro
        # informar os valores dos atributos que contabilizam os erros nas classes 'Partido', 'Prefeito' e 'Vereador'
        pass