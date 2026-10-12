import sys
from eleicao import Eleicao, Partido, Eleitor, Prefeito, Vereador, Urna, ErroCadastro

def ler_eleitores(caminho, eleicao):
    with open(f'input/{caminho}', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha.startswith(('ELEITOR:', 'VEREADOR:', 'PREFEITO:')):
                tipo, dados = linha.split(':', 1)
                campos = [i.strip() for i in dados.split(',')]
                nome, cpf, nascimento, titulo, zona, secao = campos[0], campos[1], campos[2], campos[3], campos[4], campos[5]
                try:
                    if tipo == 'ELEITOR':
                        eleitor = Eleitor(nome, cpf, nascimento, titulo, zona, secao)
                    else:
                        num_partido = campos[7]
                        partido = eleicao.buscar_partido(num_partido)
                        if partido is None:
                            raise ErroCadastro(tipo.capitalize(), 'partido', num_partido)
                        if tipo == 'VEREADOR':
                            numero, bairro, projeto_lei = campos[6], campos[8], campos[9]
                            eleitor = Vereador(nome, cpf, nascimento, titulo, zona, secao, numero, partido, bairro, projeto_lei)
                        else:
                            numero, cpf_vice, plano_governo = campos[6], campos[8], campos[9]
                            eleitor = Prefeito(nome, cpf, nascimento, titulo, zona, secao, numero, partido, cpf_vice, plano_governo)
                    eleicao.inserir_eleitor(eleitor)
                except ErroCadastro as erro:
                    eleicao.inserir_erro(erro)

def ler_partidos(caminho, eleicao):
    with open(f'input/{caminho}', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha.startswith('PARTIDO:'):
                _, dados = linha.split(':', 1)
                campos = [i.strip() for i in dados.split(',')]
                numero, sigla, nome, cnpj = campos[0], campos[1], campos[2], campos[3]
                try:
                    partido = Partido(numero, sigla, nome, cnpj)
                    eleicao.inserir_partido(partido)
                except ErroCadastro as erro:
                    eleicao.inserir_erro(erro)

def ler_urnas(caminho, eleicao):
    with open(f'input/{caminho}', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha.startswith('VOTO:'):
                _, dados = linha.split(':', 1)
                campos = [i.strip() for i in dados.split(',')]
                zona, secao, cargo, numero = campos[0], campos[1], campos[3], campos[4]

                urna = eleicao.buscar_urna(zona, secao)
                if urna is None:
                    urna = Urna(zona, secao)
                    eleicao.inserir_urna(urna)
                urna.registrar_voto(cargo, numero)

def gerar_relatorios(eleicao):
    relatorios = {
        'eleitores': eleicao.relatorio_eleitores(),
        'erros': eleicao.relatorio_erros(),
        'geral': eleicao.relatorio_geral(),
        'partidos': eleicao.relatorio_partidos(),
        'urnas': eleicao.relatorio_urnas(),
    }
    for nome, texto in relatorios.items():
        with open(f'output/{nome}.out', 'w', encoding='utf-8') as arquivo:
            arquivo.write(texto)

def main():
    if len(sys.argv) != 4:
        print("Uso: python3 app.py Partidos.txt Eleitores.txt Urnas.txt")
        sys.exit(1)

    eleicao = Eleicao()
    ler_partidos(sys.argv[1], eleicao)
    ler_eleitores(sys.argv[2], eleicao)
    ler_urnas(sys.argv[3], eleicao)
    gerar_relatorios(eleicao)


if __name__ == "__main__":
    main()