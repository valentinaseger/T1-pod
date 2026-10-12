from .prefeito import Prefeito
from .vereador import Vereador
from .urna import Urna
from .partido import Partido
from .eleitor import Eleitor
from .candidato import Candidato
from .excecoes import ErroCadastro

class Eleicao():
    SEPARADOR = ('-' * 40) +'\n'
    def __init__(self) -> None:
        self.eleitores: list[Eleitor] = []
        self.partidos: list[Partido] = []
        self.urnas: list[Urna] = []
        self.erros: list[ErroCadastro] = []
        self._prefeitos: dict[str, Prefeito] = {}
        self._vereadores: dict[str, Vereador] = {}

    def inserir_eleitor(self, eleitor: Eleitor) -> None:
        self.eleitores.append(eleitor)
        if isinstance(eleitor, Prefeito):
            self._prefeitos[eleitor.numero] = eleitor
        elif isinstance(eleitor, Vereador):
            self._vereadores[eleitor.numero] = eleitor
    def inserir_partido(self, partido: Partido) -> None:
        self.partidos.append(partido)
    def inserir_urna(self, urna: Urna) -> None:
        self.urnas.append(urna)
    def inserir_erro(self, erro: ErroCadastro) -> None:
        self.erros.append(erro)

    def buscar_eleitor(self, titulo_eleitor: str) -> Eleitor | None:
        for eleitor in self.eleitores:
            if eleitor.titulo_eleitor == titulo_eleitor:
                return eleitor
        return None
    def buscar_candidato(self, numero: str, tipo: str) -> Candidato | None:
        if tipo == 'prefeito':
            return self._prefeitos.get(numero)
        elif tipo == 'vereador':
            return self._vereadores.get(numero)
        return None
    def buscar_partido(self, numero: str) -> Partido | None:
        for partido in self.partidos:
            if partido.numero == numero:
                return partido
        return None
    def buscar_urna(self, zona: str, secao: str) -> Urna | None:
        for urna in self.urnas:
            if urna.zona == zona and urna.secao == secao:
                return urna
        return None

    def unifica_urnas(self) -> Urna:
        urna_unificada = Urna(None, None)
        for urna in self.urnas:
            urna_unificada = urna_unificada + urna
        return urna_unificada

    def filtra_validos(self, votos: dict[str, int], tipo: str) -> dict[str, int]:
        # retorna os votos dos candidatos, sem votos nulos e brancos
        filtrado = {}
        for candidato, qtd in votos.items():
            if candidato == "":
                pass
            elif self.buscar_candidato(candidato, tipo) is None:
                pass
            else:
                filtrado[candidato] = qtd
        return filtrado

    def contar_votos(self, dict_votos: dict[str, int], tipo_candidato: str) -> tuple[int, int, int]:
        brancos = 0
        nulos = 0
        validos = 0
        for num_candidato, qtd_votos in dict_votos.items():
            if num_candidato == "":
                brancos += qtd_votos
            elif self.buscar_candidato(num_candidato, tipo_candidato) is None:
                nulos += qtd_votos
            else:
                validos += qtd_votos
        return validos, nulos, brancos

    def relatorio_eleitores(self) -> str:
        total_eleitores = len(self.eleitores)

        candidatos_prefeito = 0
        candidatos_vereador = 0
        for eleitor in self.eleitores:
            if isinstance(eleitor, Prefeito):
                candidatos_prefeito += 1
            elif isinstance(eleitor, Vereador):
                candidatos_vereador += 1

        texto_final = f'{self.SEPARADOR}Relatório de Eleitores \n{self.SEPARADOR}' \
                    f'Eleitores: {total_eleitores}\n' \
                    f'Candidatos a prefeito: {candidatos_prefeito}\n' \
                    f'Candidatos a vereador: {candidatos_vereador}\n'

        dic_zonas: dict[str, dict[str, int]] = {}
        for eleitor in self.eleitores:
            zona = eleitor.zona
            secao = eleitor.secao

            if not(zona in dic_zonas):
                dic_zonas[zona] = {}
            if not(secao in dic_zonas[zona]):
                dic_zonas[zona][secao] = 0
            dic_zonas[zona][secao] += 1

        for zona in sorted(dic_zonas, key=int):
            string = f'\nZona {zona}:\n'
            secoes = dic_zonas[zona]
            for secao in sorted(secoes, key=int):
                string += f' - Seção {secao}: {secoes[secao]} eleitores\n'
            texto_final += string

        return texto_final + self.SEPARADOR
    
    def relatorio_partidos(self) -> str:
        total_partidos = len(self.partidos)

        texto_final = f'{self.SEPARADOR}Relatório de Partidos \n{self.SEPARADOR}' \
                f'Total de Partidos: {total_partidos}\n'

        for partido in self.partidos:
            qtd_prefeito = 0
            qtd_vereador = 0
            for prefeito in self._prefeitos.values():
                if prefeito.partido == partido:
                    qtd_prefeito += 1
            for vereador in self._vereadores.values():
                if vereador.partido == partido:
                    qtd_vereador += 1

            texto_final += f'\n{partido.nome} ({partido.sigla}):\n' \
                            f' - Prefeitos candidatos: {qtd_prefeito}\n' \
                            f' - Vereadores candidatos: {qtd_vereador}\n'

        return texto_final + self.SEPARADOR
    
    def relatorio_urnas(self) -> str:
        texto_final = ''
        for urna in sorted(self.urnas, key=lambda u: (int(u.zona), int(u.secao))):
            tipo_candidato = 'prefeito'
            qtd_validos_prefeito, qtd_nulos_prefeito, qtd_brancos_prefeito = self.contar_votos(urna.votos_prefeito, tipo_candidato)

            tipo_candidato = 'vereador'
            qtd_validos_vereador, qtd_nulos_vereador, qtd_brancos_vereador = self.contar_votos(urna.votos_vereador, tipo_candidato)

            texto_final += f'{self.SEPARADOR}Relatório da Urna - Zona {urna.zona} - Seção {urna.secao} \n{self.SEPARADOR}' \
                            f'Votos para prefeito: \n' \
                            f' - Válidos: {qtd_validos_prefeito}\n' \
                            f' - Brancos: {qtd_brancos_prefeito}\n' \
                            f' - Nulos: {qtd_nulos_prefeito}\n' \
                            f'Votos para vereador: \n' \
                            f' - Válidos: {qtd_validos_vereador}\n' \
                            f' - Brancos: {qtd_brancos_vereador}\n' \
                            f' - Nulos: {qtd_nulos_vereador}\n' \
                            f'{self.SEPARADOR}\n'
        return texto_final

    def relatorio_geral(self) -> str:
        texto_final = f'{self.SEPARADOR}Relatório Geral da Eleicao \n{self.SEPARADOR}'

        urna_unificada = self.unifica_urnas()
        validos_prefeito = self.filtra_validos(urna_unificada.votos_prefeito, 'prefeito')
        total_votos_validos_prefeito = sum(validos_prefeito.values())

        ranking_prefeito = sorted(validos_prefeito.items(), key=lambda item: item[1], reverse=True)

        if len(ranking_prefeito) == 0:
            texto_final += 'Nenhum voto válido para prefeito\n'
        else:
            numero_vencedor, votos_vencedor = ranking_prefeito[0]
            empate = len(ranking_prefeito > 1) and ranking_prefeito[1][1] == votos_vencedor
            if votos_vencedor >= total_votos_validos_prefeito / 2 and not empate:
                prefeito = self.buscar_candidato(numero_vencedor, 'prefeito')
                texto_final += f'Prefeito eleito: {prefeito.nome}\n\n'
            else:
                texto_final += 'Prefeito: Segundo Turno\n\n'

        ranking_vereador: list[tuple[Vereador, int]] = []
        for eleitor in self.eleitores:
            if isinstance(eleitor, Vereador):
                votos = urna_unificada.votos_vereador.get(eleitor.numero, 0)
                ranking_vereador.append((eleitor, votos))
        ranking_vereador.sort(key=lambda item: item[1], reverse=True)

        texto_final += 'Vereadores eleitos: \n'
        for vereador, votos in ranking_vereador[:10]:
            texto_final += f' - {vereador.nome}: {votos} votos\n'

        return texto_final + self.SEPARADOR
            
    def relatorio_erros(self) -> str:
        texto = ''
        for erro in self.erros:
            texto += f'{erro}\n'
        texto += f'\n{self.SEPARADOR}Relatório de Erros \n{self.SEPARADOR}' \
                f'Partidos com nome ou CNPJ inválido: {Partido.erros_validacao}\n' \
                f'Candidatos a prefeito com número inválido: {Prefeito.erros_validacao}\n' \
                f'Candidatos a vereador com número inválido: {Vereador.erros_validacao}\n'
        return texto + self.SEPARADOR