# language: pt
Funcionalidade: Pesquisa de servicos no Portal gov.br
  Como um cidadao brasileiro
  Quero pesquisar por servicos publicos
  Para encontrar rapidamente a informacao que preciso

  Contexto:
    Dado que eu acesso a pagina inicial do Portal gov.br

  Cenario: Pesquisar por um servico valido
    Quando eu pesquiso pelo termo "Imposto de Renda"
    Entao a pagina de resultados deve ser exibida

  Esquema do Cenario: Pesquisar por diferentes servicos publicos
    Quando eu pesquiso pelo termo "<servico>"
    Entao a pagina de resultados deve ser exibida

    Exemplos:
      | servico    |
      | Passaporte |
      | CNH        |
      | CPF        |

  Cenario: Submeter a busca sem informar um termo
    Quando eu submeto a busca sem informar um termo
    Entao o campo de busca deve estar visivel
