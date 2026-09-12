# Organizador de Projetos Musicais

Sistema de linha de comando para gerenciar meus projetos de produção musical
— artista, status, prazo e situação de pagamento de cada um. Criei para
resolver um problema real: eu estava esquecendo detalhes de projetos em
andamento, e queria algo simples para centralizar isso.

## Sobre o uso de IA

Todo o código deste projeto foi escrito por mim. Usei o Claude (Anthropic)
como apoio para debugar erros, entender conceitos novos (manipulação de
arquivos, JSON, funções) e revisar minha lógica ao longo do desenvolvimento.

## Funcionalidades

- **Adicionar projeto** — cadastra nome do projeto, artista, status,
  prazo e situação de pagamento
- **Listar projetos** — mostra todos os projetos cadastrados, numerados
- **Alterar projeto** — edita qualquer campo de um projeto existente
- **Apagar projeto** — remove um projeto da lista
- **Persistência em JSON** — todos os dados são salvos automaticamente
  a cada alteração, em `projetos.json`, então nada se perde ao fechar
  o programa

## Como rodar

```bash
python organizador_de_projetos.py
```

Na primeira execução, o arquivo `projetos.json` ainda não existe — o
programa começa com uma lista vazia e cria o arquivo automaticamente
na primeira vez que uma alteração é salva.

## Estrutura de cada projeto

```json
{
  "projeto": "Single Casa Monstro",
  "artista": "VINITHE4REAL",
  "status": "Mixagem",
  "prazo": "15/10/2026",
  "pagamento": "Pago"
}
```

Exemplo de projeto finalizado:

```json
{
  "projeto": "F*** Muito",
  "artista": "B Original ft. Nebbrugg",
  "status": "Finalizado",
  "prazo": "01/09/2025",
  "pagamento": "Pago"
}
```

Os campos **status** e **pagamento** têm opções pré-definidas (ex:
Composição, Gravação, Mixagem...) mas também aceitam um valor
personalizado através da opção "Outro" em cada menu.

## Conceitos praticados

- Funções com retorno e parâmetros (inclusive parâmetros com valor padrão)
- Leitura e escrita de arquivos JSON (`json.load` / `json.dump`)
- Tratamento de exceções (`FileNotFoundError`, `ValueError`, `IndexError`)
- Listas de dicionários como estrutura de dados
- Referência de objetos em memória (edição direta de itens da lista)

## Próximos passos (melhorias planejadas)

- [ ] Filtrar/buscar projetos por status
- [ ] Suportar mais de um artista por projeto (feats/colaborações)
- [ ] Ordenar projetos por prazo
- [ ] Unificar os menus de status e pagamento em uma função genérica