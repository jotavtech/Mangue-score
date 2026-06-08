# Mangue Score — Projeto BDD de QA (VA02 · P5)

Automacao de testes de interface (UI) no **Portal gov.br** — um site governamental
publico — utilizando **Cypress + Cucumber + Gherkin** (BDD).

> Disciplina: Qualidade de Software (QA) — Projeto VA02 / P5
> Tema: Testes BDD em site governamental publico

---

## Objetivo

Garantir, de forma automatizada e legivel por qualquer pessoa (Gherkin em portugues),
o funcionamento correto de cenarios essenciais do Portal gov.br:

- Acesso e carregamento da pagina inicial;
- Validacao dos elementos principais (menu, busca, secao de servicos);
- Pesquisa por servicos publicos (cenario com dados / `Esquema do Cenario`);
- Navegacao ate a pagina de servicos.

---

## Tecnologias

| Ferramenta | Uso |
|------------|-----|
| [Cypress](https://www.cypress.io/) `13.x` | Execucao dos testes E2E/UI |
| [@badeball/cypress-cucumber-preprocessor](https://github.com/badeball/cypress-cucumber-preprocessor) | Suporte a Cucumber/Gherkin no Cypress 13+ |
| [@bahmutov/cypress-esbuild-preprocessor](https://github.com/bahmutov/cypress-esbuild-preprocessor) | Empacotamento dos steps com esbuild |
| Gherkin (pt) | Escrita dos cenarios em linguagem natural |

---

## Estrutura do projeto

```
Mangue-score/
├── cypress/
│   ├── e2e/
│   │   ├── features/                 # Cenarios em Gherkin (.feature)
│   │   │   ├── acessoPortal.feature
│   │   │   ├── pesquisa.feature
│   │   │   └── navegacaoServicos.feature
│   │   └── steps/                    # Implementacao dos passos
│   │       ├── acessoPortalSteps.js
│   │       ├── pesquisaSteps.js
│   │       └── navegacaoServicosSteps.js
│   ├── fixtures/
│   │   └── dados.json                # Massa de dados de apoio
│   ├── pages/                        # Page Objects (boa pratica)
│   │   ├── portal.page.js
│   │   ├── pesquisa.page.js
│   │   └── servicos.page.js
│   └── support/
│       ├── commands.js               # Comandos customizados (ex.: aceitarCookies)
│       └── e2e.js
├── cypress.config.js                 # Config do Cypress + plugin do Cucumber
├── package.json
└── README.md
```

---

## Como executar

### 1. Pre-requisitos
- [Node.js](https://nodejs.org/) (versao LTS recomendada)
- npm

### 2. Instalar dependencias
```bash
npm install
```

### 3. Executar os testes

**Modo interativo (abre a interface do Cypress):**
```bash
npm run cypress:open
```

**Modo headless (linha de comando, gera video):**
```bash
npm run cypress:run
```

**Executar um unico arquivo de feature:**
```bash
npx cypress run --spec "cypress/e2e/features/pesquisa.feature"
```

Os videos das execucoes ficam em `cypress/videos/` e os relatorios em
`cypress/reports/` (HTML e JSON gerados pelo preprocessor do Cucumber).

---

## Cenarios automatizados

### `acessoPortal.feature` — Acesso ao Portal gov.br
- Carregar a pagina inicial com sucesso;
- Validar elementos principais (menu, busca, secao de servicos).

### `pesquisa.feature` — Pesquisa de servicos
- Pesquisar por um servico valido;
- `Esquema do Cenario` (data-driven): Passaporte, CNH, CPF;
- Submeter a busca sem informar um termo.

### `navegacaoServicos.feature` — Navegacao
- Acessar a pagina de servicos e validar a URL e o campo de busca.

---

## Boas praticas aplicadas

- **Page Objects**: seletores e acoes centralizados em `cypress/pages/`, reduzindo
  duplicacao e facilitando manutencao.
- **Gherkin em portugues** (`# language: pt`): cenarios legiveis para todo o time.
- **Steps reutilizaveis**: passos compartilhados (ex.: acesso a home, campo de busca
  visivel) definidos uma unica vez.
- **Fixtures**: massa de dados separada em `cypress/fixtures/dados.json`.
- **Comando customizado** `aceitarCookies` tolerante a ausencia do banner.
- **Seletores resilientes** e `retries` configurados, dado que sites governamentais
  podem variar layout/conteudo.

---

## Observacao

Sites governamentais sao ambientes reais e podem sofrer alteracoes de layout,
indisponibilidade temporaria ou protecoes anti-bot. Os seletores foram escritos da
forma mais resiliente possivel; caso o portal mude, ajuste os Page Objects em
`cypress/pages/`.

---

## Equipe

Projeto desenvolvido para a disciplina de QA — VA02 / P5.

Repositorio: https://github.com/jotavtech/Mangue-score
