# GabrielleValentina

## Como usar o app
1. Coloque os arquivos de entrada na pasta `Input/`, seguindo o formato:

   **Partidos.txt**
```
   PARTIDO: numero,sigla,nome,cnpj
```

   **Eleitores.txt**
```
   ELEITOR: nome,cpf,nascimento,titulo,zona,secao
   VEREADOR: nome,cpf,nascimento,titulo,zona,secao,numero,partido,bairro,projeto_de_lei
   PREFEITO: nome,cpf,nascimento,titulo,zona,secao,numero,partido,cpf_vice,plano_de_governo
```
   - `partido` é o número do partido do candidato (para prefeito, 2 dígitos; para vereador, 5 dígitos).
   - `nome` precisa ter até 50 caracteres.
   - `cnpj` precisa ser 14 dígitos.
   - `cpf` e `cpf_vice` precisam ser 11 dígitos.

   **Urnas.txt**
```
   VOTO: zona,secao,cpf,cargo,numero
```
   - `cargo` deve ser `PREFEITO` ou `VEREADOR`;
   - `numero` vazio conta como voto em branco;
   - número que não corresponde a nenhum candidato conta como voto nulo.

2. Na pasta raiz do projeto, rode:
```
   python3 app.py Partidos.txt Eleitores.txt Urnas.txt
```

3. Os relatórios são gerados na pasta `output/`: `eleitores.out`, `partidos.out`, `urnas.out`, `geral.out` e `erros.out`.

## O pacote `eleicao`
- `Partido`, `Eleitor`, `Candidato` (abstrata), `Prefeito` e `Vereador`: cadastro, com validação dos campos;
- `Urna`: registra os votos; duas urnas podem ser somadas com `+`;
- `Eleicao`: guarda tudo, faz as buscas e gera os relatórios;
- `ErroCadastro`: exceção lançada quando algum campo é inválido.