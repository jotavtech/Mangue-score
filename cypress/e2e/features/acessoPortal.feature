# language: pt
Funcionalidade: Acesso ao Portal gov.br
  Como um cidadao brasileiro
  Quero acessar a pagina inicial do Portal gov.br
  Para utilizar os servicos publicos do Governo Federal

  Contexto:
    Dado que eu acesso a pagina inicial do Portal gov.br

  Cenario: Carregar a pagina inicial com sucesso
    Entao o titulo da pagina deve conter "gov.br"
    E o campo de busca deve estar visivel

  Cenario: Validar elementos principais da pagina inicial
    Entao devo visualizar o menu de navegacao
    E devo visualizar a secao de servicos
