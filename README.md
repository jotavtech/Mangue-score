# Mangue Score

Repositorio com dois projetos distintos:

1. **Projeto BDD QA (VA02 · P5)** — Automacao de testes E2E no Portal gov.br com Cypress + Cucumber + Gherkin
2. **MangueScore** — Classificador Musical Manguebeat em Python

---

## Projeto BDD QA — Cypress + Cucumber + Gherkin

Automacao de testes de interface (UI) no **Portal gov.br** utilizando **Cypress 13 + Cucumber + Gherkin (BDD)**.

> Disciplina: Qualidade de Software (QA) — Projeto VA02 / P5

### Tecnologias

| Ferramenta | Uso |
|------------|-----|
| [Cypress](https://www.cypress.io/) `13.x` | Execucao dos testes E2E/UI |
| [@badeball/cypress-cucumber-preprocessor](https://github.com/badeball/cypress-cucumber-preprocessor) | Suporte a Cucumber/Gherkin no Cypress 13+ |
| Gherkin (pt) | Cenarios em linguagem natural |

### Estrutura

```
├── cypress/
│   ├── e2e/
│   │   ├── features/          # Cenarios em Gherkin
│   │   │   ├── acessoPortal.feature
│   │   │   ├── pesquisa.feature
│   │   │   └── navegacaoServicos.feature
│   │   └── steps/             # Implementacao dos passos
│   ├── fixtures/dados.json
│   ├── pages/                 # Page Objects
│   └── support/
├── cypress.config.js
└── package.json
```

### Como executar os testes

```bash
npm install
npm run cypress:open    # modo interativo
npm run cypress:run     # modo headless (gera video)
```

### Cenarios (8 testes, todos verdes)

- **acessoPortal**: carregar a home + validar menu, campo de busca e secao de servicos
- **pesquisa**: busca valida + `Esquema do Cenario` (data-driven: Passaporte, CNH, CPF) + busca vazia
- **navegacaoServicos**: acessar `/pt-br/servicos` e validar a URL e o titulo da pagina

### Boas praticas aplicadas

- **Page Objects**: seletores centralizados em `cypress/pages/`
- **Gherkin em portugues** (`# language: pt`)
- **Steps reutilizaveis** entre cenarios
- **Fixtures** para massa de dados
- **Comando customizado** `aceitarCookies` tolerante a ausencia do banner

---

## MangueScore — Classificador Musical

Classificador que identifica o DNA Manguebeat em musicas e artistas.

### Stack

- Python 3.8+
- pytest

### Como rodar

```bash
pip install -r requirements.txt
python -m pytest -v
python -m pytest --cov=src --cov-report=html
```

### Estrutura Python

```
src/
├── models/musica.py
└── services/manguescore_calculator.py
tests/unit/
├── test_musica.py
└── test_manguescore_calculator.py
```

---

Repositorio: https://github.com/jotavtech/Mangue-score
